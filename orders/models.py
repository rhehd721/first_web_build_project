from django.db import models


class Order(models.Model):

    """ Order models """

    book = models.ForeignKey("essays.Essays", on_delete=models.CASCADE)  # 주문 할 책 가져오기
    user_name = models.CharField(max_length=50)  # 주문자 이름
    address = models.CharField(max_length=150, null=False)  # 주문자 주소
    book_count = models.IntegerField(null=False)  # 책 구매 개수
    price = models.IntegerField()  # 가격
