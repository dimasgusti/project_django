from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Function-based view for the post list
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),  # Post detail view
    path('<int:post_id>/share/', views.post_share, name='post_share'),  # Correct URL pattern for sharing
    path(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list,name='post_list_by_tag'),
]