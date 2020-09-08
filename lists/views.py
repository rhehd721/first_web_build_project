from django.shortcuts import render, redirect
from django.utils import timezone
from .models import List


# 일기 작성
def create(request):

    """ create views 일기 작성 """

    if request.method == "POST":
        post = List()

        post.name = request.POST["title"]  # 제목
        post.user = request.POST["user"]  # 작성자
        post.now = request.POST["date"]
        post.content = request.POST["message"]  # 내용

        post.save()

        return redirect("detail")

    return render(request, "list/create.html")


def detail(request):

    page = List.objects.all()  # 모든 리스트 객체 가져오기
    page.now = timezone.now()

    return render(request, "list/list.html", {"page": page})
