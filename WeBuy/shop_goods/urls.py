from django.conf.urls import url,include
from . import views

urlpatterns = [
    # url(r'^show/$',views.show),
    url(r'^$', views.index),
    url(r'^index/$',views.index),
    url(r'^Products/$',views.Products),
    url(r'^getGoodsType(\d+?)/$',views.getGoodsType),
    url(r'^getGoodsType(\d+?)/(\d+?)/$',views.getGoodsType),
    url(r'^getGoods(\d+)/$',views.getGoods),
    url(r'^Product(\d+)/$',views.Product),
    url(r'^clickNumber/$',views.clickNumber),
]