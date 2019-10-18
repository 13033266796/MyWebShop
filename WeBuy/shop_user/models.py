from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user_name = models.CharField(max_length=20,null=True)
    user_pwd = models.CharField(max_length=40)
    user_number = models.CharField(max_length=11)#手机号
    user_nickname = models.CharField(max_length=20,null=True)
    user_mail = models.CharField(max_length=20,null=True)
    user_address = models.CharField(max_length=100,default='请选择省,请选择市,请选择县,详细地址')
    user_telephone = models.IntegerField(max_length=12,null=True)#固定电话
    user_youbian = models.CharField(max_length=6,null=True)
    user_score = models.CharField(max_length=100,default='0')
    user_money = models.CharField(max_length=100,default='0')
    user_gender = models.BooleanField(default=True)#默认为男性True


    def __str__(self):
        return self.user_nickname

class AreaInfo(models.Model):
    name = models.CharField(max_length=50)
    ad_code = models.CharField(max_length=15)
    city_code = models.CharField(max_length=50, null=True, blank=True)
    center = models.CharField(max_length=50)
    level = models.CharField(max_length=15)
    parent_ad_code = models.ForeignKey('self', null=True, blank=True)
