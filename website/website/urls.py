from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/blog/')),  # Redirect root to /blog/
    path('blog/', include('blog.urls', namespace='blog')),  # Include the blog URLs
]