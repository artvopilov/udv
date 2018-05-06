from django.contrib import admin
from django.urls import path
from server.views import (
    get_by_id_udv_user,
    get_all_udv_user,
    get_by_moderator_id_article,
    insert_udv_user,
    get_by_id_article
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/by-id/', get_by_id_udv_user),
    path('api/users/', get_all_udv_user),
    path('api/users/insert', insert_udv_user),
    path('api/articles/by-moderator-id/', get_by_moderator_id_article),
    path('api/articles/by-id/', get_by_id_article),
]
