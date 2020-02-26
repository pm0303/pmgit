# Author: pm
# Time: 2020/2/21 9:08
# FileName: myfun.py

# 自定义过滤器

# 导入过滤器
from django.template import Library
from ..models import Article, Category, Tag

register = Library()


@register.filter
def mydateFormat(data):
    return "%d-%d-%d" % (data.year, data.month, data.day)


@register.filter
def authorFormat(author, info):
    return info + ":" + author.upper()


@register.simple_tag
def get_latestarticles(num=3):
    return Article.objects.all().order_by("-create_time")[:num]


@register.simple_tag
def get_latesdates(num=3):
    datas = Article.objects.dates("create_time", "month", "DESC")[:num]
    print(datas)
    return datas


@register.simple_tag
def get_categorys():
    return Category.objects.all().order_by("-id")


@register.simple_tag
def gettags():
    return Tag.objects.all().order_by("-id")
