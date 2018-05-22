from django.http import (JsonResponse,
                         HttpResponseBadRequest,
                         HttpResponse,
                         HttpResponseRedirect)
from ..models import UdvUser
import json
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.views.decorators.csrf import csrf_exempt


def get_by_id(request):
    if request.method == "GET":
        user_id = request.GET.get('user_id')
        if user_id is None:
            return HttpResponseBadRequest("No user_id provided")
        user = UdvUser.get_by_id(1).values()
        return JsonResponse(user, safe=False)

    if request.method == "PUT":
        return HttpResponse()

    return HttpResponseBadRequest("Request method must be GET")


def get_all(request):
    if request.method == "GET":
        users = list(UdvUser.get_all().values())
        return JsonResponse(users, safe=False)

    return HttpResponseBadRequest(reason="Request method must be GET")


def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
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
