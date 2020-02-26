# Author: pm
# Time: 2020/2/24 17:11
# FileName: urls.py
from django.conf.urls import url
from . import views

app_name = 'blogs'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^favicon.ico/$', views.favicon),

]
