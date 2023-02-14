from django.contrib import admin
from django.urls import path, include

from webapp.views.articles import add_view
from webapp.views.base import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
    path("", index_view),
    path("article/add/", add_view)
]
