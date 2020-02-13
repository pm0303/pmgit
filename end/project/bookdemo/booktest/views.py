from django.shortcuts import render

# 导入模板
from django.template import loader
from .models import Book, Hero
# Create your views here.
# 在自出接收请求 处理数据 返回响应

from django.http import HttpResponse


def index(request):
    # return HttpResponse("这里是首页")
    # 获取模板
    # template = loader.get_template('index.html')
    # # 2.渲染模板数据
    books = Book.objects.all()
    context = {"books", books}
    # result = template.render(context)
    # # 3.将渲染的结果使用HttpResponse
    # return HttpResponse(result)
    return render(request, 'index.html', {"books": books})


def about(request):
    return HttpResponse("这里是关于页面")


def detail(request, bookid):
    # return HttpResponse("这里是详情页"+bookid)
    # template = loader.get_template('detail.html')
    book = Book.objects.get(id=bookid)
    # context = {"book": book}
    # result = template.render(context)
    # return HttpResponse(result)
    return render(request, 'detail.html', {"book": book})
# 使用django模板
# MVT
