from rest_framework import viewsets

from .models import *
from .serializers import *


class CategoryViewSets(viewsets.ModelViewSet):
    """
    分类试图
    继承ModelViewSet 之后拥有GET POST PUT PATCH DELETE等HTTP动词操作
    queryset  指明 需要操作的模型列表
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
