from django.conf.urls import url
from .views import *

urlpatterns = [
    url('home/', index, name='home'),
    url(r'adduser/', adduser, name='adduser'),
    url(r'add_position/', add_position, name='add_position'),
    url(r'create_user/', create_user, name='create_user'),
    url(r'worker/([0-9]{1})/', show_worker, name='worker'),
    url(r'show_cats/([0-9]{1})/', show_cats, name='show_cats')
]