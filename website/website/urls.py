from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),  # Include the blog URLs
    path('', RedirectView.as_view(url='/blog/')),  # Redirect root to /blog/
]