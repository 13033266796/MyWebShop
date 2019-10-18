from django.db import models
from shop_user.models import UserInfo


# Create your models here.

class OrderInfo(models.Model):
    order_code = models.CharField(max_length=20,primary_key=True)
    user_name = models.ForeignKey('shop_user.UserInfo')
    total_pay = models.DecimalField(max_digits=7,decimal_places=2)
    order_time = models.DateTimeField(auto_now=True)
    user_address = models.CharField(max_length=40)
    pass

class orderGoods(models.Model):
    goods_name = models.ForeignKey('shop_goods.GoodsInfo')
    belong_order = models.ForeignKey(OrderInfo)
    pay = models.DecimalField(max_digits=6,decimal_places=2)
    count = models.IntegerField()
    pass


