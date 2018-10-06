from rest_framework import serializers
from .models import Bookinfo, Authors, Translators


# 將書籍資料表序列化
class BookinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookinfo
        fields = ('_id', 'book_image', 'book_name_ch',
                  'book_name_fore', 'publisher', 'pub_time', 'pub_contry', 'isbn', 'pub_category',
                  'first_category', 'second_category', 'third_category', 'spec', 'lang', 'content', 'table_of_content',
                  'au', 'trans')

# 將作者資料表序列化
class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ('_id', 'author_ch', 'author_fore', 'author_intro')

# 將譯者資料表序列化
class TranslatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translators
        fields = ('_id', 'translator_name', 'translator_intro')
