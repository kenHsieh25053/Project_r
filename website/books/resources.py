from import_export import resources
from .models import Bookinfo, Authors, Translators

# 定義需要匯出的資料表(書籍資訊)
class BookinfoResources(resources.ModelResource):
    class Meta:
        model = Bookinfo

# 定義需要匯出的資料表(作者資訊)
class AuthorsResources(resources.ModelResource):
    class Meta:
        model = Authors

# 定義需要匯出的資料表(譯者資訊)
class TranslatorsResources(resources.ModelResource):
    class Meta:
        model = Translators
