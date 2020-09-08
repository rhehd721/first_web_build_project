from django.db import models
from core import models as core_models
from groups import models as groups_models

# Create your models here.


class List(core_models.TimeStempedModel):  # 일기
    now = models.DateTimeField(auto_now_add=True)  # 일기 날짜
    #    weather = models.ImageField() # 일기 날씨
    title = models.CharField(max_length=20, null=True)  # 일기 제목
    content = models.TextField(default="", blank=True)  # 일기 내용
    photos = models.ImageField(upload_to="list_photos", null=True)  # 사진
    name = models.CharField(max_length=20, null=True)

    # 외래키
    groups = models.ForeignKey(
        groups_models.Group, related_name="list", on_delete=models.CASCADE
    )

