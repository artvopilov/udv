from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from ..models import Article, Paragraph, BlockOfText, AlternativeOpinion, Source, UdvUser
import json, datetime


def get_by_id(request):
    if request.method == 'GET':
        article_id = request.GET.get('id')
        if article_id is None:
            return HttpResponseBadRequest("No id was provided")
        article = Article.get_by_id(article_id)
        article_json = to_json(article)
        return JsonResponse(article_json, safe=False)

    return HttpResponseBadRequest("Request method must be GET")


def get_by_moderator_id(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        if user_id is None:
            return HttpResponseBadRequest("No user_id provided")
        article = Article.get_by_moderator_id(user_id)
        article_json = to_json(article)
        return JsonResponse(article_json, safe=False)

    return HttpResponseBadRequest("Request method must be GET")


def propose_new_article(request):
    if request.method != 'POST':
        return HttpResponseBadRequest("Request method must be POST")
    if not request.user.is_authenticated:
        return HttpResponseBadRequest("User must be authenticated")
    try:
        data = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        return HttpResponseBadRequest("invalid json")

    if not Validator.article(data):
        return HttpResponseBadRequest("Not all parameters provided")

    try:
        parent = Article.get_by_id(data['parent_id'])
    except Article.DoesNotExist:
        return HttpResponseBadRequest("parent does not exist")

    a = Article.objects.create(creator=UdvUser.objects.get(id=request.user.id),
                               title=data['title'], parent=parent, moderator=parent.moderator)
    # TODO all source properties
    for index, paragraph_json in enumerate(data['paragraphs']):
        paragraph = Paragraph.objects.create(article=a, subtitle=paragraph_json['subtitle'], number=index)
        for blk_index, blk in enumerate(paragraph_json['blocks']):
            opinion = AlternativeOpinion.objects.create(paragraph=paragraph)
            source = Source.objects.create(link=blk['source']['url'], author=blk['source']['author'],
                                           char_number=0, date_upload=datetime.datetime.now())  # TODO charnumber
            block = BlockOfText.objects.create(source=source, text=blk['text'], alternative_opinion=opinion,
                                               number=blk_index)

    return HttpResponse("%d" % a.id)


def propose_change(request):
    if request.method != 'PATCH':
        return HttpResponseBadRequest("Request method must be PATCH")
    if not request.user.is_authenticated:
        return HttpResponseBadRequest("User must be authenticated")
    try:
        data = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        return HttpResponseBadRequest("invalid json")

    if not Validator.changes(data):
        return HttpResponseBadRequest("Not all parameters provided")

    try:
        changed = BlockOfText.objects.get(id=data['block_id'])  # который запрашивается на изменение
    except BlockOfText.DoesNotExist:
        return HttpResponseBadRequest("paragraph does not exist")

    blk = data['new_version']
    source = Source.objects.create(link=blk['source']['url'], author=blk['source']['author'],
                                   char_number=0, date_upload=datetime.datetime.now())  # TODO charnumber
    block = BlockOfText.objects.create(source=source, text=blk['text'], is_main=False,
                                       alternative_opinion=changed.alternative_opinion, number=changed.number)
    changed.alternative_opinion.paragraph.article.status = Article.CHANGED

    return HttpResponse("OK")


def to_json(article):
    return {
        "id": article.id,
        "title": article.title,
        "status": article.status,
    }


class Validator:
    article_structure = {'parent_id': int, 'title': str, 'paragraphs': list}
    paragraph_structure = {'subtitle': str, 'blocks': list}
    block_structure = {'text': str, 'source': dict}
    source_structure = {'author': str, 'url': str}

    @classmethod
    def block(cls, data):
        return cls.check_structure(data, cls.block_structure) \
               and cls.check_structure(data['source'], cls.source_structure)

    @classmethod  # valid.block is more self explaining then cls.block
    def paragraph(valid, data):
        return valid.check_structure(data, valid.paragraph_structure) and \
               all(map(valid.block, data['blocks']))

    @classmethod
    def changes(valid, data):
        return valid.check_structure(data, {'block_id': int, 'new_version': dict}) \
               and valid.block(data['new_version'])

    @classmethod
    def article(valid, data):
        return valid.check_structure(data, valid.article_structure) and \
               all(map(valid.paragraph, data['paragraphs']))

    @staticmethod
    def check_structure(data, struct):
        """
        >>> s = {'hello' : 1, 'a' : {}, 'z' : []}
        >>> Validator.check_structure(s, {'hello' : int, 'a' : dict, 'z' : list})
        True
        >>> Validator.check_structure(s, {'hello' : int, 'a' : dict, 'z' : str})
        False
        """
        return all(map(lambda key: isinstance(data.get(key), struct[key]), struct))
