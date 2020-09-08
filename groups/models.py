import random
from django.db import models
from core import models as core_models


class Group(core_models.TimeStempedModel):

    """ Groups Model """

    name = models.CharField(max_length=150) # 그룹 이름
    uni_code = models.IntegerField(null=True) # 그룹 고유 값 입력받기 
    image = models.ImageField(upload_to='images/') # 책 표지 정하기
    members = models.ManyToManyField("accounts.User", related_name="group", blank=True) # User 객체

    def __str__(self):
        return self.name
