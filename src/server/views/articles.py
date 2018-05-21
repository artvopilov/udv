from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from ..models import Article
import json


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


def insert(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if not article_is_valid(data):
            return HttpResponseBadRequest("Not all parameters provided")
        Article.insert(data['creator'], data['title'], data['moderator'], data['parent'])
        return HttpResponse("Ok")

    return HttpResponseBadRequest("Request method must be POST")


def to_json(article):
    return {
        "id": article.id,
        "title": article.title,
        "status": article.status,
    }


def article_is_valid(data):
    if not all(k in data for k in ('creator', 'title', 'moderator', 'parent')):
        return False
    return True
