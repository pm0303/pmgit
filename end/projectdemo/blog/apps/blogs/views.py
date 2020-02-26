from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from .forms import CommnetForm
from .models import *


# Create your views here.
def index(request):
    # return HttpResponse("这是首页")
    artilce = Article.objects.all().order_by("-create_time")

    return render(request, 'index.html', locals())


def detail(request, articleid):
    # return HttpResponse("这是详情页"+qid)
    if request.method == "GET":
        try:
            article = Article.objects.get(id=articleid)
            cf = CommnetForm()
            return render(request, 'single-post.html', locals())
        except Exception as e:
            print(e)
            return HttpResponse("文章错误")
    elif request.method == "POST":
        cf = CommnetForm(request.POST)
        if cf.is_valid():
            print(cf)
            commnet = cf.save(commit=False)
            commnet.article = Article.objects.get(id=articleid)
            commnet.save()
            url = reverse("blogs:detail", args=(articleid,))
            return redirect(to=url)
        else:
            article = Article.objects.get(id=articleid)
            cf = CommnetForm()
            return render(request, 'single-post.html', locals())


def contact(request):
    # return HttpResponse("这是联系我们")
    return render(request, 'contact.html')


def favicon(request):
    url = '/static/favicon.ico'
    return redirect(to=url)
