from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """ Custom user Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"

    # tuple
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )

    name = models.CharField(max_length=50, default="멋쟁이")
    avatar = models.ImageField(blank=True)  # 프로필사진
    gender = models.CharField(  # 성별
        choices=GENDER_CHOICES,
        max_length=10,
        blank=True,
        default=GENDER_MALE,  # choices 의 default 값
    )

    age = models.IntegerField(null=True)  # 나이
