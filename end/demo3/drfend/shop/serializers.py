# Author: pm
# Time: 2020/2/26 15:41
# FileName: serializers.py
from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    """
    编写针对Category的序列化类
    本类指明了Category的序列化细节
    需要继承才可以针对模型进行序列化
    在 Meta  model 指定序列化模型  fields 指明序列化字段
    """
    # 与定义的model.py中的 releated_name一致
    # StringRelatedField() 可以显示关联模型中的__str__返回值
    # many=True 代表多个对象 一对一时可以不用写
    goods = serializers.StringRelatedField(many=True)
    # goods = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # goods = serializers.HyperlinkedRelatedField(view_name='good-detail', read_only=True, many=True)

    class Meta:
        model = Category
        fields = "__all__"


class GoodSerializer(serializers.ModelSerializer):
    # 在序列化中指定字段 再多方 使用  source = 模型名 字段名 read_only指明不能更改
    category_super = serializers.CharField(source='category', read_only=True)

    class Meta:
        model = Good
        # fields = "__all__"
        fields = ('name', 'desc', 'category', 'category_super')
