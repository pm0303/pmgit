from django.contrib import admin

# Register your models here.
# Django自带的后台管理


# 注册自己需要管理的模型
from .models import Book, Hero

admin.site.register(Book)
admin.site.register(Hero)
