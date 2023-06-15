from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='blog/index', permanent=True)),
    path('admin/', admin.site.urls),
    path('blog/', include('Blog.urls')),
]
