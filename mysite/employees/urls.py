from django.conf.urls import url
from .views import *

urlpatterns = [
    url('home/', index, name='home'),
    url(r'adduser/', adduser, name='adduser'),
    url(r'addposition/', add_position, name='add_position'),
    url(r'create_position/([0-9]+)/', create_position, name='create_position'),
    url(r'create_user/([0-9]+)/', create_user, name='create_user'),
    url(r'worker/([0-9]+)/', show_worker, name='worker'),
    url(r'show_cats/([0-9]+)/', show_cats, name='show_cats'),
    url(r'del_worker/([0-9]+)/', del_worker, name='del_worker'),
    url(r'del_position/([0-9]+)/', del_position, name='del_position'),
]