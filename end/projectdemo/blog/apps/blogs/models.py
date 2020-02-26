from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.

class Ads(models.Model):
    img = models.ImageField(upload_to='ads', verbose_name="首图")
    desc = models.CharField(max_length=20, verbose_name="描述")

    def __str__(self):
        return self.desc


class Article(models.Model):
    title = models.CharField(max_length=20, verbose_name="标题")
    # article = models.TextField(max_length=200, verbose_name="文章")
    article = UEditorField(imagePath='imgs/', width='100%')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateField(auto_now_add=True, verbose_name="更新时间")
    author = models.CharField(max_length=15, verbose_name="作者")
    views = models.PositiveIntegerField(default=0, verbose_name="阅读量")
    public = models.ForeignKey('Public', on_delete=models.CASCADE, verbose_name="共有内容")
    img = models.ImageField(upload_to='article_imgs', default=0, verbose_name="图片")
    author_img = models.ImageField(upload_to="author_imgs",default=0, verbose_name="作者头像")

    def __str__(self):
        return self.title


class Commnet(models.Model):
    name = models.CharField(max_length=20, verbose_name="评论人")
    email = models.EmailField(default="2641938505@qq.com", verbose_name="个人邮箱")
    body = models.CharField(max_length=200, verbose_name="评论内容")
    url = models.URLField(default="http://www.baidu.com", verbose_name="评论来源")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="所属文章")

    def __str__(self):
        return self.name


class Public(models.Model):
    title = models.CharField(max_length=20, verbose_name="标题")
    introduction = models.CharField(max_length=200, verbose_name="简介")
    img = models.ImageField(upload_to='public', verbose_name="公共图片")

    def __str__(self):
        return self.title
