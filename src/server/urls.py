from django.urls import path
from .views import (
    get_by_id_udv_user,
    get_all_udv_user,
    get_by_moderator_id_article,
    register_udv_user,
    get_by_id_article,
    insert_article,
    login_user
)


urlpatterns = [
    path('users/by-id/', get_by_id_udv_user),
    path('users/', get_all_udv_user),
    path('users/register', register_udv_user),
    path('articles/by-moderator-id/', get_by_moderator_id_article),
    path('articles/by-id/', get_by_id_article),
    path('articles/insert/', insert_article),
    path('login/', login_user),
    path('register/', register_udv_user)
]