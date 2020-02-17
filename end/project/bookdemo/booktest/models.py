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
    price = models.FloatField(default=0)

    def __str__(self):
        return self.title


class Hero(models.Model):
    """
    hero 继承Model 也可以操作数据库
    """
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='male')
    content = models.CharField(max_length=100)
    # book 是一对多中的外键 on_delete代表删除主表数据是如何删除
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# 自定义模型管理类
class UserManager(models.Manager):
    def deleteByTelePhone(self, tele):
        user = self.get(telephone=tele)
        user.delete()

    def createUser(self, tele):
        # self model()可以获取模型类构造函数
        user = self.model()
        # user = User() 相当于 user = self.model()
        user.telephone = tele
        user.save()


class User(models.Model):
    telephone = models.CharField(max_length=11, null=True, blank=True, verbose_name="手机号")
    manage = UserManager()

    def __str__(self):
        return self.telephone

    class Meta:
        db_table = "用户类"

        ordering = ["telephone"]
        # admin页面进入模型显示类显示名字
        verbose_name = "用户模型"
        # admin 页面在应用下方显示的模型名
        verbose_name_plural = "用户模型类"


class Account(models.Model):
    username = models.CharField(max_length=20, verbose_name="用户名")
    password = models.CharField(max_length=20, verbose_name="密码")
    regist_date = models.DateField(auto_now_add=True, verbose_name="注册日期")


class Concact(models.Model):
    telephone = models.CharField(max_length=11, verbose_name="手机号")
    email = models.EmailField(default="2641938505@qq.com")
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="con")


class Article(models.Model):
    title = models.CharField(max_length=20, verbose_name="标题")
    sumary = models.TextField(verbose_name="正文")


class Tag(models.Model):
    name = models.CharField(max_length=10, verbose_name="标签名")
    articles = models.ManyToManyField(Article)




# django orm关联查询 关键字段只定义在多方
# 多方Hero   一方Book
# 1多找一， 多方对象.关系字段    exp: h1.book
# 2一找多， 一方对象.小写多方类名_set.all()   exp:  b1.hero_set.all()


# 一对一 示例 Acount 实例 a Concact 实例c 关系字段在任意一方
# a 找 c a.+类名(concact)
# c 找 a  c.account
# 如果定义了related_name 实例 a.con

# 多对多 多方Article 实例a 多方 Tag 实例 t 关系字段吧可以定义在任意一方
# 添加关系 t.articles.add(a)   移出关系 t.articles.remove(a)
