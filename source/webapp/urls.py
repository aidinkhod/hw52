from django.contrib import admin
from django.urls import path

import webapp.views.base
from webapp.views.articles import add_view, detail_view
from webapp.views.base import index_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", webapp.views.base.index_view),
    path("article/", detail_view)
]