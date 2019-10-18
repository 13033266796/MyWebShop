from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^registered/$',views.register),
    url(r'^registerPost/$',views.registerPost),
    url(r'^Login/$',views.Login),
    url(r'^Logout/$',views.Logout),
    url(r'^checkVerifyCode/$',views.checkVerifyCode),
    url(r'^verifyCode/$',views.verifyCode),
    url(r'^LoginPost/$',views.LoginPost),
    url(r'^user/$',views.user),
    url(r'^user_info/$',views.user_info),
    url(r'^user_infoPost/$',views.user_infoPost),
    url(r'^user_Password/$',views.user_Password),
    url(r'^updatePwdPost/$',views.updatePwdPost),
    url(r'^headPost/$',views.headPost),
    url(r'^checkHead/$',views.checkHead),
    url(r'^user_address/$',views.user_address),
    url(r'^pro/$',views.pro),
    url(r'^cityAndDis(\d+?)/$',views.cityAndDis),
    url(r'^addressPost/$',views.addressPost),
    url(r'^user_Collect(\d*)/$',views.user_Collect),
    url(r'^user_integral/$',views.user_integral),



]