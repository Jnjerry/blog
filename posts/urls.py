from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	)

urlpatterns = [
	url(r'^list/$', post_list,name='list'),
    url(r'^create/$', post_create),
    url(r'^detail/(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^update/(?P<id>\d+)/$', post_update, name='update'),
    url(r'^delete/(?P<id>\d+)/$', post_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
