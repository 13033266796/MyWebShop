from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^order(\d+)/$',views.order),
    url(r'^createOrder/$',views.createOrder),
    url(r'getOrderGoods(\d+)/$',views.getOrderGoods),
    url(r'^getMyOrder/$',views.getMyOrder),

]