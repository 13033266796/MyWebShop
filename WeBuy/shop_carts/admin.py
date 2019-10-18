from django.contrib import admin
from .models import CartsInfo,CollectInfo

# Register your models here.
admin.site.register(CartsInfo,admin.ModelAdmin)
admin.site.register(CollectInfo,admin.ModelAdmin)