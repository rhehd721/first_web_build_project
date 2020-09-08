from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path("list/", views.detail, name="detail"),
    path("create/", views.create, name="create"),
]
