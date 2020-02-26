# Author: pm
# Time: 2020/2/24 9:52
# FileName: search_indexes.py

from haystack import indexes
# 指明搜索模型为article
from .models import Article


# 1.类名必须为 模型名Index
# 2.get_model必须为
class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
