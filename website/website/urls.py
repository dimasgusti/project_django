from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/blog/')),  
    path('blog/', include('blog.urls', namespace='blog')), 
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]