from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
#    url(r'^test-404/$', 'core.views.error404'),
    url(r'^contactus/$', views.contactus, name='contactus'),
    url(r'^products/$',views.products,name='products'),
    url(r'^product/detail/$',views.product_detail,name='product_detail'),
    url(r'^$', views.index, name='index'),
)
