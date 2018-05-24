from django.urls import path
from .views import (
    get_by_id_udv_user,
    get_all_udv_user,
    get_by_moderator_id_article,
    register_udv_user,
    get_by_id_article,
    propose_new_article,
    propose_change,
    login_user,
    logout_user,
    make_moderator,
    get_subscribed
)


urlpatterns = [
    path('users/by-id/', get_by_id_udv_user),
    path('users/', get_all_udv_user),
    path('users/register', register_udv_user),
    path('articles/by-moderator-id/', get_by_moderator_id_article),
    path('articles/by-id/', get_by_id_article),
    path('articles/insert/', propose_new_article),
    path('articles/change/', propose_change),
    path('users/make-moderator', make_moderator),
    path('users/get-subscribed', get_subscribed),
    path('login', login_user),
    path('register', register_udv_user),
    path('logout', logout_user)
]