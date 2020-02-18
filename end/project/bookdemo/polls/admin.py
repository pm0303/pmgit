from django.contrib import admin

# Register your models here.

from .models import Qusetion, Choices,User


class ChoiceInline(admin.StackedInline):
    """
    定义关联类
    """
    model = Choices
    extra = 1


class ChoicesAdmin(admin.ModelAdmin):
    pass


class QuestionAdmin(admin.ModelAdmin):
    # list_display = [""]
    inlines = [ChoiceInline]


admin.site.register(Qusetion, QuestionAdmin)
admin.site.register(Choices, ChoicesAdmin)
admin.site.register(User)