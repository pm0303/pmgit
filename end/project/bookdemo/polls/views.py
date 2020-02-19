from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import *
# Create your views here.
from django.views.generic import View, TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView as DV
from django.contrib.auth import authenticate, login as lin, logout as lot
from .forms import *


# 登录
def login(request):
    if request.method == "GET":
        # lf = LoginForm()
        # return render(request, 'polls/login.html', {"lf": lf})
        # 方法一html中form表单
        return render(request, 'polls/login.html')
    elif request.method == "POST":
        # lf = LoginForm(data=request.POST)
        # if lf.is_valid():
        #     username = lf.cleaned_data["username"]
        #     password = lf.cleaned_data["password"]

        username = request.POST.get("username")
        password = request.POST.get("password")
        # 可以使用Django自带的用户认证系统
        user = authenticate(username=username, password=password)
        if user:
            lin(request, user)
            next = request.GET.get("next")
            if next:
                url = next
            else:
                url = reverse("polls:index")
            return redirect(to=url)
        else:
            # url = reverse("polls:login")
            # return redirect(to=url)
            return render(request, "polls/login.html", {"errors": "用户密码不匹配"})
        # else:
        #     return HttpResponse("未知错误")
    # return HttpResponse("登录")


# 退出
def loginout(request):
    # 调用Django的登出方法 目的是删除cookie
    lot(request)
    url = reverse("polls:index")
    return redirect(to=url)


# 注册
def regist(request):
    if request.method == "GET":
        #1. 使用html 生成表单
        return render(request, 'polls/regist.html')
        # 3.使用模型表单类
        # rf =  RegistForm()
        # return render(request,'polls/regist.html',{"rf":rf})

    else:
        # rf = RegistForm(request.POST)
        # if rf.is_valid():
        #     print(rf,"++")
        #     username = rf.cleaned_data["username"]
        #     password = rf.cleaned_data["password"]
        #     password2 = rf.cleaned_data["password2"]
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if User.objects.filter(username=username).count() > 0:
            # return HttpResponse("用户名已存在")
            return render(request, 'polls/regist.html', {"errors": "用户名已存在"})
        else:
            if password == password2:
                User.objects.create_user(username=username, password=password)
                # rf.save()
                url = reverse("polls:login")

                return redirect(to=url)

            else:
                # return HttpResponse("密码不一致")
                return render(request, 'polls/regist.html', {"errors": "密码不一致"})
        # else:
        #     return HttpResponse("未知错误")

def index(request):
    question = Qusetion.objects.all()
    return render(request, 'polls/index.html', {"question": question})
    # return HttpResponse("首页")


# 基于CBV形式实现
class IndexView(ListView):
    # 方法二、继承ListView
    # template_name指明使用的模板
    template_name = "polls/index.html"
    # queryset 指明返回的结果列表
    queryset = Qusetion.objects.all()
    # context_object_name 指明返回字典参数的健
    context_object_name = "question"

    # 方法一、继承的TemplateView
    # template_name = "polls/index.html"
    # def get_context_data(self, **kwargs):
    #     return {"questions":Question.objects.all()}


# 详情页
def detail(request, qid):
    print(qid, "+++")
    if request.method == "GET":
        print("当前用户为", request.user)
        if request.user and request.user.username != "":
            #     已经登录过了
            print(request.user.questions.all())
            try:
                question = Qusetion.objects.get(id=qid)
                if question in request.user.questions.all():
                    # print("投过票")
                    url = reverse("polls:result", args=(qid))
                    return redirect(to=url)

                else:
                    try:
                        # question = Qusetion.objects.get(id=qid)
                        print(question, "--")
                        return render(request, 'polls/detail.html', {"question": question})

                    except Exception as e:
                        print(e)
                        return HttpResponse("问题不合法")
            except Exception as e:
                print(e)
        else:
            url = reverse("polls:login") + "?next=/polls/detail/" + qid + "/"
            return redirect(to=url)
    elif request.method == "POST":
        choiceid = request.POST.get("num")
        try:
            choice = Choices.objects.get(id=choiceid)
            choice.votes += 1
            choice.save()
            request.user.questions.add(Qusetion.objects.get(id=qid))
            # 返回当前投票问题的投票结果页
            url = reverse("polls:result", args=(qid,))
            # 投票成功 返回投票结果
            return redirect(to=url)

        except:
            return HttpResponse("选项不合法")

    # return HttpResponse("详情页"+qid)


class DetailView(View):
    def get(self, request, qid):
        try:
            question = Qusetion.objects.get(id=qid)
            print(question, "--")
            return render(request, 'polls/detail.html', {"question": question})

        except Exception as e:
            print(e)
            return HttpResponse("问题不合法")

    def post(self, request, qid):
        choiceid = request.POST.get("num")
        try:
            choice = Choices.objects.get(id=choiceid)
            choice.votes += 1
            choice.save()
            # 返回当前投票问题的投票结果页
            url = reverse("polls:result", args=(qid,))
            # 投票成功 返回投票结果
            return redirect(to=url)

        except:
            return HttpResponse("选项不合法")


# 结果页
def result(request, qid):
    try:
        question = Qusetion.objects.get(id=qid)
        return render(request, 'polls/result.html', {"question": question})
    except Exception as e:
        print(e)
        return HttpResponse("问题不合法")


class ResultView(DV):
    # 方法一: 继承View
    def get(self, request, qid):
        try:
            question = Qusetion.objects.get(id=qid)
            return render(request, 'polls/result.html', {"question": question})
        except Exception as e:
            print(e)
            return HttpResponse("问题不合法")
