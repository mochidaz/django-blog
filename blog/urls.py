from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.static import serve

from blog import settings
from .views import IndexView, SearchView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView, name="home"),
    path('blog/', include("article.urls")),
    path('search/', SearchView, name="search"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    ]
