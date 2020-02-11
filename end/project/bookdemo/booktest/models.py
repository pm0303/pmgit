from django.db import models


# Create your models here.

# 在此处编写应用的数据模型类
# 每一张表就是一个模型类


class Book(models.Model):
    """
    book继承Model类 应为  Model类拥有操作数据库的功能
    """
    title = models.CharField(max_length=20)
    pub_date = models.DateField(default="2020-02-11")


class Hero(models.Model):
    """
    hero 继承Model 也可以操作数据库
    """
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='male')
    price = models.FloatField(default=0)
    content = models.CharField(max_length=100)
    # book 是一对多中的外键 on_delete代表删除主表数据是如何删除
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
