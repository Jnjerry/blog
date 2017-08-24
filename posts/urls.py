from django.conf.urls import url
from .import views



urlpatterns = [
	url(r'^list/$', views.PostListView.as_view(),name='list'),
    url(r'^create/$', views.post_create,name='create'),
    url(r'^detail/(?P<pk>\d+)$', views.PostListDetail.as_view(), name='detail'),
    url(r'^edit/(?P<pk>\d+)$', views.post_edit, name='post_edit'),
    url(r'^delete/(?P<pk>\d+)/$', views.post_delete),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
	url(r'^$', views.home,name='index'),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
