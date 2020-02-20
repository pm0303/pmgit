from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .urls import *
from .models import *

# 导入django分页器
from django.core.paginator import Page, Paginator


# 一个 Page中有object_list代表当前页的所有对象
# has_next   是否有下一页
# has_previous    是否有上一页
# next_page_number    下一页
# previous_page_number   上一页
# self.number    当前页编号
# self.paginator   当前页分页器

# 一个 Paginator中的object_list   代表所有未分页对象
# self.per_page   每一页有几个对象
# get_page(self,number)  从分页器中去第几页
# page_range(self)    返回分页列表
# Create your views here.

# 首页
def index(request):
    ads = Ads.objects.all()
    articles = Article.objects.all()
    paginator = Paginator(articles, 2)
    # 获取get请求中的页码参数，默认为1
    num = request.GET.get("pagenum", 1)
    page = paginator.get_page(num)
    return render(request, 'index.html', {"ads": ads, "page": page})
    # return HttpResponse("首页")
    # return render(request, 'index.html', locals())
    # 获取当前作用域的局部变量
    # print(locals())


# 详情页
def detail(request, articleid):
    # return HttpResponse("详情页" + articleid)
    return render(request, 'single.html')


# 反馈页面
def contact(request):
    # return HttpResponse("联系我们")
    return render(request, 'contact.html')


# 添加图标
def favicon(request):
    url = '/static/favicon.ico'
    return redirect(to=url)
