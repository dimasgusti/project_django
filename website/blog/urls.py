from django.urls import path, re_path
from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'), 
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'), 
    path('<int:post_id>/share/', views.post_share, name='post_share'), 
    re_path(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'), 
    path('feed/', LatestPostsFeed(), name='post_feed'),
]