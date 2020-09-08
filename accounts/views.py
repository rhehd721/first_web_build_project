from django.shortcuts import render, redirect
from .models import User
from django.contrib import auth

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("group_main") # 그룹 선택 화면 이동
        else:
            print("로그인안댐")
            return render(request, "account/join.html", {"error": "아이디 또는 비밀 번호가 다릅니다."})
    else:
        print("로그인안댐")
        return render(request, "account/join.html")


def logout(request):
    auth.logout(request)
    return redirect("login")


def signup(request):
    if request.method == "POST":
        if request.POST.get("password1") == request.POST.get("password2"):
            user = User.objects.create_user(
                username=request.POST.get("username"), password=request.POST.get("password1")
            )
            # 유저 값을 가져와 아이디/패스워드에 추가한 값을 user에 추가
            auth.login(request, user)
            return redirect('login')  # 다시 로그인 화면
        print("생성 안됌") 
        return render(request, "")  # 비밀번호 확인 실패 시 다시 돌아감.
    
    print("생성 안됌")
    return render(request, "")  # POST 형식 아닐 시


def about(request): # 소개페이지
    return render(request,'about.html')