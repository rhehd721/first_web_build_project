from django.shortcuts import render, redirect
from accounts.models import User 
from .models import Group 
# Create your views here.

def group_home(request):
    groups = Group.objects.all() # 모든 그룹 리스트 출력
    return render(request, "groups/main.html",{'groups':groups})

def group_create(request):
    if request.method == 'POST':
        group = Group()
        group.image = request.FILES['image'] # new.html의 name="image"
        group.name = request.POST['name'] # new.html의 name="name"
        group.save()
        print("생성완료")
        return redirect('group_main')
    print("생성실패") 
    return render(request, 'groups/makegroup.html')