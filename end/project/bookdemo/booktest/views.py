from django.shortcuts import render, redirect, reverse

# 导入模板
from django.template import loader
from .models import Book, Hero
# Create your views here.
# 在自出接收请求 处理数据 返回响应

from django.http import HttpResponse, HttpResponseRedirect


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
    # return HttpResponse("++")
    # return HttpResponse("这里是详情页"+bookid)
    # template = loader.get_template('detail.html')
    book = Book.objects.get(id=bookid)
    # context = {"book": book}
    # result = template.render(context)
    # return HttpResponse(result)
    return render(request, 'detail.html', {"book": book})


def deletebook(request, bookid):
    book = Book.objects.get(id=bookid)
    book.delete()
    # 重定向
    # return HttpResponseRedirect(redirect_to='/')
    # return redirect(to='/')
    # 解除硬编码
    url = reverse("booktest:index")
    return redirect(to=url)


def deletehero(request, heroid):
    hero = Hero.objects.get(id=heroid)
    bookid = hero.book.id
    hero.delete()

    # 解除硬编码
    url = reverse('booktest:detail', args=(bookid,))
    return redirect(to=url)

# 添加书籍
def addbook(request):
    if request.method == "GET":
        return render(request, 'addbook.html')
    elif request.method == "POST":
        book = Book()
        book.title = request.POST.get("booktitle")
        book.pub_date = request.POST.get("bookpub_date")
        book.price = request.POST.get("bookprice")
        book.save()
        url = reverse("booktest:index")
        return redirect(to=url)
# 编辑书籍
def editbook(request,bookid):
        book = Book.objects.get(id =bookid)
        if request.method == "GET":
            return render(request,"editbook.html",{"book":book})
        elif request.method == "POST":
            book.title = request.POST.get("booktitle")
            book.price = request.POST.get("bookprice")
            book.pub_date = request.POST.get("bookpub_date")
            book.save()
            url = reverse("booktest:index",args=(bookid,))
            return redirect(to=url)
# 添加英雄
def addhero(request, bookid):
    if request.method == "GET":
        return render(request, 'addhero.html')
    elif request.method == "POST":
        hero = Hero()
        hero.name = request.POST.get("heroname")
        hero.content = request.POST.get("herocontent")
        hero.gender = request.POST.get("sex")
        hero.book = Book.objects.get(id=bookid)
        hero.save()
        url = reverse("booktest:detail", args=(bookid,))
        return redirect(to=url)

# 编辑英雄
def edithero(request, heroid):
    hero = Hero.objects.get(id = heroid)
    # 使用get方法进入编辑页面
    if request.method == "GET":
        return render(request, 'edithero.html', {"hero": hero})
    elif request.method == "POST":
        hero.name = request.POST.get("heroname")
        hero.content = request.POST.get("herocontent")
        hero.gender = request.POST.get("sex")
        hero.save()
        url = reverse("booktest:detail", args=(hero.book.id,))
        return  redirect(to=url)
# 使用django模板
# MVT
