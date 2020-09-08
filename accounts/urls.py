from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.login, name="login"),  # 홈페이지 실행 시 로그인 창 출력
    path("logout/", views.logout, name="logout"),  # 로그아웃 페이지 이동
    path("signup/", views.signup, name="signup"),  # 회원가입 페이지 이동
    path("about/", views.about, name="about"), # about 페이지 
]
