"""drfend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from shop.views import *
# 引入自带路由类
from rest_framework import routers

router = routers.DefaultRouter()

# 可以通过router默认路由注册资源
router.register('categorys', CategoryViewSets)
router.register('goods', GoodViewSets)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include(router.urls)),
    # path('',include('shop.urls',namespace='shop')),
    # 为了路由调试界面能够使用用户相关的功能需要引入以下路由
    # 配置RestFulApi
    path('',include('rest_framework.urls'))

]
