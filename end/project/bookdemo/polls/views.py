from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import *
# Create your views here.
from django.views.generic import View, TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView as DV


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


def detail(request, qid):
    print(qid, "+++")
    if request.method == "GET":
        try:
            question = Qusetion.objects.get(id=qid)
            print(question, "--")
            return render(request, 'polls/detail.html', {"question": question})

        except Exception as e:
            print(e)
            return HttpResponse("问题不合法")
    elif request.method == "POST":
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

    # return HttpResponse("详情页"+qid)

class DetailView(View):
    def get(self,request,qid):
        try:
            question = Qusetion.objects.get(id=qid)
            print(question, "--")
            return render(request, 'polls/detail.html', {"question": question})

        except Exception as e:
            print(e)
            return HttpResponse("问题不合法")
    def post(self,request,qid):
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


def result(request, qid):
    try:
        question = Qusetion.objects.get(id=qid)
        return render(request, 'polls/result.html', {"question": question})
    except Exception as e:
        print(e)
        return HttpResponse("问题不合法")

class ResultView(DV):
    # 方法一: 继承View
    def get(self,request,qid):
        try:
            question = Qusetion.objects.get(id=qid)
            return render(request, 'polls/result.html', {"question": question})
        except Exception as e:
            print(e)
            return HttpResponse("问题不合法")