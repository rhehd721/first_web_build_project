from django.db import models
from core import models as core_models

# Create your models here.
class Comment(core_models.TimeStempedModel):  # 일기 댓글
    name = models.ForeignKey("accounts.User", on_delete=models.CASCADE)  # 사용자 이름
    content = models.CharField(max_length=30)  # 댓글 내용
    lists = models.ForeignKey(
        "lists.List", related_name="comment", on_delete=models.CASCADE
    )  # 연결할 일기

