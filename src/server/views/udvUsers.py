from django.http import (JsonResponse,
                         HttpResponseBadRequest,
                         HttpResponse,
                         HttpResponseRedirect)
from ..models import UdvUser, Article
import json
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


def get_by_id(request):
    if request.method == "GET":
        user_id = request.GET.get('user_id')
        if user_id is None:
            return HttpResponseBadRequest("No user_id provided")
        user = UdvUser.get_by_id(user_id).__dict__
        user = {key: user[key] for key in ('email', 'first_name', 'last_name', 'occupation', 'age')}

        return JsonResponse(user, safe=False)

    if request.method == "PUT":
        return HttpResponse()

    return HttpResponseBadRequest("Request method must be GET")


def get_all(request):
    if request.method == "GET":
        users = list(UdvUser.get_all().values())
        return JsonResponse(users, safe=False)

    return HttpResponseBadRequest(reason="Request method must be GET")


def make_moderator(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if 'candidate_id' not in data:
            return HttpResponseBadRequest(reason="candidate_id must be provided")
        if request.user is None or not request.user.is_super_moderator:
            return HttpResponseBadRequest(reason="Only super moderator is able to make user moderator")
        candidate_id = data["candidate_id"]
        candidate = UdvUser.get_by_id(candidate_id)
        UdvUser.make_moderator(candidate)
        return HttpResponse("Ok")
    return HttpResponseBadRequest(reason="Request method must be POST")


def get_subscribed(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponseBadRequest(reason="User must be authenticated")
        data = json.loads(request.body)
        if 'article_id' not in data:
            return HttpResponseBadRequest(reason="Article id is not provided")
        article = Article.get_by_id(data['article_id'])
        if article is None:
            return HttpResponseBadRequest(reason="Article with id {} is not found".format(data['article_id']))
        request.user.subscribe(article)
        return HttpResponse("Ok")

    return HttpResponseBadRequest(reason="Request method must be POST")


def login_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            return HttpResponseBadRequest("invalid json")
        email = data["email"]
        password = data["password"]
        user = authenticate(username=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("Ok")
        return HttpResponseBadRequest(reason="Auth failed")
    return HttpResponseBadRequest(reason="Request must be POST",  content="Request must be POST")


def logout_user(request):
    try:
        logout(request)
        return HttpResponse("Ok")
    except:
        return HttpResponseBadRequest("Logout went wrong")


def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if not udv_user_is_valid(data):
            return HttpResponseBadRequest("Not all parameters provided")
        UdvUser.insert(data['password'], data['email'], data['first_name'], data['last_name'])
        udv_user = authenticate(username=data['email'], password=data['password'])
        if udv_user is None:
            return HttpResponseBadRequest("Auth went wrong")
        login(request, udv_user)
        return HttpResponse("Ok")

    return HttpResponseBadRequest(reason="Request must be POST")


def udv_user_is_valid(data):
    if not all(k in data for k in ('first_name', 'last_name', 'password', 'email')):
        return False
    return True
