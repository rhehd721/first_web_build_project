from django.urls import path
from . import views

urlpatterns = [
    path("groupmain/", views.group_home, name="group_main"),  # 그룹 나열 페이지  
    path("groupcreate/", views.group_create, name="group_create"), # 그룹 생성 페이지
]
