from django.contrib import admin
from .models import GoodsInfo,GoodsType
# Register your models here.

class myAdmin(admin.ModelAdmin):
    list_filter = ['goods_type']

admin.site.register(GoodsType,admin.ModelAdmin)
admin.site.register(GoodsInfo,myAdmin)