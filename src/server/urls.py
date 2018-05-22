from django.urls import path
from .views import (
    get_by_id_udv_user,
    get_all_udv_user,
    get_by_moderator_id_article,
    register_udv_user,
    get_by_id_article,
    insert_article,
<<<<<<< HEAD
    propose_change,
    login_user
=======
    login_user,
    logout_user
>>>>>>> afaf89e2bfdaa35168cd2f85c52c863c68f476c9
)


urlpatterns = [
    path('users/by-id/', get_by_id_udv_user),
    path('users/', get_all_udv_user),
    path('users/register', register_udv_user),
    path('articles/by-moderator-id/', get_by_moderator_id_article),
    path('articles/by-id/', get_by_id_article),
    path('articles/insert/', insert_article),
<<<<<<< HEAD
    path('articles/change/', propose_change),
    path('login/', login_user),
    path('register/', register_udv_user)
=======
    path('login', login_user),
    path('register', register_udv_user),
    path('logout', logout_user)
>>>>>>> afaf89e2bfdaa35168cd2f85c52c863c68f476c9
]