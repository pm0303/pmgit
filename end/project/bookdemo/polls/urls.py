# Author: pm
# Time: 2020/2/17 11:34
# FileName: urls.py

from django.conf.urls import url
from . import views

app_name = "polls"

urlpatterns = [
    # url(r'^$',views.index,name='index'),
    # url(r'^detail/(\d+)/$',views.detail,name='detail'),
    # url(r'^result/(\d+)/$',views.result,name='result')
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^detail/(\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^result/(\d+)/$', views.ResultView.as_view(), name='result')
]
