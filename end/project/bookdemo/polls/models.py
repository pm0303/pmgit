from django.db import models


# Create your models here.

class Qusetion(models.Model):
    title = models.CharField(max_length=50, verbose_name="投票问题")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-create_date"]
        verbose_name = "投票表"
        verbose_name_plural = verbose_name


class Choices(models.Model):
    content = models.CharField(max_length=50, verbose_name="选项")
    votes = models.PositiveIntegerField(verbose_name="得票数",default=0)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    question = models.ForeignKey(Qusetion, on_delete=models.CASCADE, related_name="choices", verbose_name="所属问题")

    def __str__(self):
        return self.content

    class Meta:
        ordering = ["-create_time"]
        verbose_name = "选项表"
        verbose_name_plural = "选项表"
