from django.db import models

# Create your models here.

class CartsInfo(models.Model):
    user_name = models.ForeignKey('shop_user.UserInfo')
    goods_name = models.ForeignKey('shop_goods.GoodsInfo')
    productsNumber = models.IntegerField()

    def __str__(self):
        return self.user_name.user_nickname

class CollectInfo(models.Model):
    user_name = models.ForeignKey('shop_user.UserInfo')
    goods_name = models.ForeignKey('shop_goods.GoodsInfo')
