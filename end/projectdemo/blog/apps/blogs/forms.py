# Author: pm
# Time: 2020/2/25 19:28
# FileName: forms.py
from django import forms
from .models import Commnet


class CommnetForm(forms.ModelForm):
    class Meta:
        model = Commnet
        fields = ["name", "url", "email", "body"]
        labels = {
            "name": "名字:",
            "url": "主页:",
            "email": "邮箱:",
            "body": "正文:"
        }
        widgets = {
            "body": forms.Textarea()
        }
