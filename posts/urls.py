from django.conf.urls import url
from .import views



urlpatterns = [
	url(r'^list/$', views.PostListView.as_view(),name='list'),
    url(r'^create/$', views.post_create,name='create'),
    url(r'^detail/(?P<pk>\d+)$', views.PostListDetail.as_view(), name='detail'),
    url(r'^update/(?P<pk>\d+)$', views.post_update, name='update'),
    url(r'^delete/(?P<id>\d+)/$', views.post_delete),
	url(r'^$', views.home,name='index'),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
