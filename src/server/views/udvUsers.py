from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse, HttpResponseRedirect
from ..models import UdvUser
import json
from django.contrib.auth import authenticate, login, get_user_model
from django.views.decorators.csrf import csrf_exempt


def get_by_id(request):
    if request.method == "GET":
        user_id = request.GET.get('user_id')
        if user_id is None:
            return HttpResponseBadRequest("No user_id provided")
        user = UdvUser.get_by_id(1)
        user_json = to_json(user)
        return JsonResponse(user_json, safe=False)

    if request.method == "PUT":
        return HttpResponse()

    return HttpResponseBadRequest("Request method must be GET")


def get_all(request):
    if request.method == "GET":
        users_json = [to_json(user) for user in UdvUser.get_all()]
        return JsonResponse(users_json, safe=False)

    return HttpResponseBadRequest("Request method must be GET")


def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data["username"]
        password = data["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("Ok")
        return HttpResponseBadRequest("Error")


def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if not udv_user_is_valid(data):
            return HttpResponseBadRequest("Not all parameters provided")
        UdvUser.insert(data['password'], data['username'], data['email'], data['first_name'], data['last_name'])
        udv_user = authenticate(username=data['username'], password=data['password'])
        if udv_user is None:
            return HttpResponseBadRequest("Error")
        login(request, udv_user)
        return HttpResponse("Ok")

    return HttpResponseBadRequest("Request method must be POST")


def to_json(user):
    return {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "occupation": user.occupation,
        "age": user.age,
        "moderator": user.moderator
    }


def udv_user_is_valid(data):
    if not all(k in data for k in ('first_name', 'last_name', 'password', 'email', 'username')):
        return False
    return True
