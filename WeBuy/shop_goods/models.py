from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class GoodsType(models.Model):
    typeName = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    pass
    def __str__(self):
        return self.typeName

class GoodsInfo(models.Model):
    goods_name = models.CharField(max_length=40)
    goods_image = models.ImageField(upload_to='goodsImage')
    goods_price = models.DecimalField(max_digits=6,decimal_places=2)
    goods_unit = models.CharField(max_length=10)
    goods_valueNumber = models.IntegerField()
    goods_clickNumber = models.IntegerField()
    goods_originPlace = models.CharField(max_length=10)
    goods_introduction = models.CharField(max_length=100)
    goods_content = HTMLField()
    goods_type = models.ForeignKey(GoodsType)
    pass

    def __str__(self):
        return self.goods_name