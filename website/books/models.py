from django.db import models
import django_filters
# from django_filters import rest_framework


# 書籍資訊資料表
class Bookinfo(models.Model):

    # 定義資料表名稱
    class Meta(object):
        db_table = 'bookinfo'
        ordering = ['_id']
    
    # 定義個別欄位
    _id = models.AutoField(unique=True, primary_key=True, verbose_name='書籍ID')
    book_image = models.TextField(verbose_name='書籍圖片')
    book_name_ch = models.CharField(max_length=50, verbose_name='中文書名')
    book_name_fore = models.CharField(max_length=100, verbose_name='外文書名')
    publisher = models.CharField(max_length=30, verbose_name='出版社')
    pub_time = models.CharField(max_length=10, verbose_name='出版日期')
    pub_contry = models.CharField(max_length=15, verbose_name='出版地')
    isbn = models.CharField(max_length=20, verbose_name='ISBN編碼')
    pub_category = models.CharField(max_length=20, verbose_name='出版社分類')
    first_category = models.CharField(max_length=20, verbose_name='分類第一層')
    second_category = models.CharField(max_length=20, verbose_name='分類第二層')
    third_category = models.CharField(max_length=20, verbose_name='分類第三層')
    spec = models.CharField(max_length=50, verbose_name='書籍規格')
    lang = models.CharField(max_length=15, verbose_name='書籍語言')
    content = models.TextField(verbose_name='書籍內容')
    table_of_content = models.TextField(verbose_name='書籍目錄')
    au = models.OneToOneField(
        'Authors', on_delete=models.CASCADE, verbose_name='作者名稱')
    trans = models.OneToOneField(
        'Translators', on_delete=models.CASCADE, verbose_name='譯者名稱')

    # 回傳書籍中文名稱用於admin和terminal顯示
    def __str__(self):
        # 如果書籍中文名稱為空，則回傳書籍外文名稱
        if Bookinfo.book_name_ch in [None, '']:
            return self.book_name_fore
        else:
            return self.book_name_ch

# 書籍資料篩選器
class BookinfoFilter(django_filters.FilterSet):
    class Meta:
        model = Bookinfo
        fields = ['book_name_ch', 'publisher',
                  'first_category', 'second_category', 'third_category']

# 作者資訊資料表
class Authors(models.Model):
    # 定義資料表名稱
    class Meta(object):
        db_table = 'authors'
        ordering = ['_id']
    
    # 定義個別欄位
    _id = models.AutoField(unique=True, primary_key=True, verbose_name='作者ID')
    author_ch = models.CharField(max_length=15, verbose_name='作者中文名')
    author_fore = models.CharField(max_length=50, verbose_name='作者外文名')
    author_intro = models.TextField(verbose_name='作者簡介')
    # book = models.ForeignKey(
    #     'Bookinfo', on_delete=models.CASCADE, verbose_name='書籍外鍵ID')

    # 回傳作者中文名稱用於admin和terminal顯示
    def __str__(self):
        # 如果作者中文名為空，則回傳作者外文名
        if Authors.author_ch in [None, '']:
            return self.author_fore
        else:
            return self.author_ch

# 作者資料篩選器
class AuthorsFilter(django_filters.FilterSet):
    class Meta:
        model = Authors
        fields = ['author_ch', 'author_fore']

# 譯者資訊資料表
class Translators(models.Model):
    class Meta(object):
        db_table = 'translators'
        ordering = ['_id']
    
    # 定義個別欄位
    _id = models.AutoField(unique=True, primary_key=True, verbose_name='譯者ID')
    translator_name = models.CharField(max_length=15, verbose_name='譯者姓名')
    translator_intro = models.TextField(verbose_name='譯者簡介')
    # book = models.ForeignKey(
    #     'Bookinfo', on_delete=models.CASCADE, verbose_name='書籍外鍵ID')

    # 回傳譯者名稱用於admin和terminal顯示
    def __str__(self):
        return self.translator_name

# 譯者資料篩選器
class TranslatorsFilter(django_filters.FilterSet):
    class Meta:
        model = Translators
        fields = ['translator_name']
