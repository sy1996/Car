from django.conf.urls import url
from carapp import views

urlpatterns = [
    url(r'^login/$',views.login),
    url(r'^zhuce/$',views.zhuce),
    url(r'^update/$',views.update),
    url(r'^index/$',views.index),
    url(r'^buycar/(\d+)/(\d+)/$',views.buycar),
    url(r'^salecar/$',views.salecar),
    url(r'^tz/$',views.tz),
    url(r'^cardetail/(\d+)/$',views.cardetail2),
    url(r'^tijiaocar/$',views.tijiaocar),
    url(r'^upload/$', views.upload),
    url(r'^paycar/$', views.pay),
    url(r'^gujia/$', views.gujia),
    url(r'^buyer/$',views.buyer)



]