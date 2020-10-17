from django.urls import path

from .views import CategoryView, PostDetail, PostView

urlpatterns = [
        path('', PostView.as_view(), name='blog'),
        path('kategori/<category>/', CategoryView, name="category"),
        path('<category>/<slug:slug>/', PostDetail, name='detail'),
]
