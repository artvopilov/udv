from django.http import JsonResponse, HttpResponseBadRequest
from ..models import Article
from .udvUsers import to_json as to_json_user


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


def to_json(article):
    return {
        "id": article.id,
        "title": article.title,
        "status": article.status,
        "moderator": to_json_user(article.moderator),
    }
