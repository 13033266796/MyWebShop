from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^shopping_cart/$',views.shopping_cart),
    url(r'^shopping_cart(\d*)/$',views.shopping_cart),
    url(r'^addToCart/$',views.addToCart),
    url(r'^head_getCartsNumber/$',views.head_getCartsNumber),
    url(r'^deleteGoods/$',views.deleteGoods),
    url(r'^deleteAllGoods/$',views.deleteAllGoods),
    url(r'^collectGoods/$',views.collectGoods),
    url(r'^light_collect/$',views.ligt_collect),
    url(r'^delete_collect/$',views.delete_collect),

]