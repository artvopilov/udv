from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from ..models import Article, Paragraph, BlockOfText, AlternativeOpinion, Source, UdvUser
from .udvUsers import to_json as to_json_user
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

# в реквесте будет json, вида
# {
#   "parent_id" : int,
#   "title" : str,
#   "paragraphs" : [
#       {
#           "subtitle" : str,
#           "blocks" : [
#               {
#                   "text" : "x",
#                   "source" : {
#                       "author": "",
#                       "url": "",
#                   },
#               },
#               {...},
#               {...},
#               {...},
#               ...
#           ]
#       },
#       {...},
#       {...},
#       {...},
#       ...
#   ]
# }
# создателем будет отправивший юзер
# модератором - модератор parent статьи
#
# пока что добавлятся будет только текст (без фоток всяких)
# добавляет в action !!
def insert(request):
    if not request.user.is_authenticated:
        return HttpResponseBadRequest("User must be logged in")
    if not request.method == 'POST':
        return HttpResponseBadRequest("Request method must be POST")

    try:
        data = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        return HttpResponseBadRequest("invalid json")

    if not article_is_valid(data):
        return HttpResponseBadRequest("Not all parameters provided")

    try:
        parent = Article.objects.get(id=data['parent_id'])
    except Article.DoesNotExist:
        return HttpResponseBadRequest("parent does not exist")

    a = Article.objects.create(creator=UdvUser.objects.get(id=request.user.id),
                title=data['title'], parent=parent, moderator=parent.moderator)
    # TODO all source properties
    for prgph in data['paragraphs']:
        paragraph = Paragraph.objects.create(article=a, subtitle=prgph['subtitle'])
        for blk in prgph['blocks']:
            opinion = AlternativeOpinion.objects.create(paragraph=paragraph)
            source = Source.objects.create(link=blk['source']['url'], author=blk['source']['author'],
                                           char_number=0, date_upload=datetime.datetime.now()) # TODO charnumber
            block = BlockOfText.objects.create(source=source, text=blk['text'], alternative_opinion=opinion)

    return HttpResponse("%d" % a.id)




def to_json(article):
    return {
        "id": article.id,
        "title": article.title,
        "status": article.status,
    }


def article_is_valid(data):
    structure = {'parent_id' : int, 'title' : str, 'paragraphs' : list }
    paragraph_structure = {'subtitle' : str, 'blocks' : list}
    block_structure = {'text' : str, 'source' : dict}
    source_structure = {'author' : str, 'url': str}
    if not check_structure(data, structure):
        return False
    for par in data['paragraphs']:
        if not check_structure(par, paragraph_structure):
            return False
        for block in par['blocks']:
            if not check_structure(block, block_structure) or not check_structure(block['source'], source_structure):
                return False
    return True


def check_structure(data, struct):
    """
    >>> s = {'hello' : 1, 'a' : {}, 'z' : []}
    >>> check_structure(s, {'hello' : int, 'a' : dict, 'z' : list})
    True
    >>> check_structure(s, {'hello' : int, 'a' : dict, 'z' : str})
    False
    """
    for k in struct:
        if not isinstance(data.get(k), struct[k]):
            return False
    return True
