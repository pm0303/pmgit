from django.contrib import admin

# 导入模块
from django.contrib.admin import ModelAdmin

# Register your models here.
# Django自带的后台管理


# 注册自己需要管理的模型
from .models import Book, Hero


class HeroInline(admin.StackedInline):
    """
    定义关联类
    """
    model = Hero
    extra = 5


class HeroAdmin(ModelAdmin):
    list_display = ('name', 'content', 'gender')


admin.site.register(Hero, HeroAdmin)


class BookAdmin(ModelAdmin):
    """
    定义模型管理类
    通过该类可以修改后台页面
    """
    list_display = ('title', 'price', 'pub_date')
    # 每页显示1页
    list_per_page = 1
    # 定义后端可搜索字段
    search_fields = ('title', 'price')
    # 定义后端过滤字段
    list_filter = ('title', 'price')

    inlines = [HeroInline]


admin.site.register(Book, BookAdmin)
