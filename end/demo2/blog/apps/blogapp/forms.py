# Author: pm
# Time: 2020/2/21 17:06
# FileName: forms.py
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name","url","email","body"]
        labels = {
            "name": "名字:",
            "url": "主页:",
            "email": "邮箱:",
            "body": "正文:"
        }
        widgets={
            "body":forms.Textarea()
        }
