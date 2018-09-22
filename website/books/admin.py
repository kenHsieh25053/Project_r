from django.contrib import admin
from .models import Bookinfo, Authors, Translators

# 設定書籍資料表在admin中相關操作
class BookinfoAdmin(admin.ModelAdmin):
    list_display = ('book_name_ch', 'publisher', 'pub_time', 'isbn', 'au', 'trans')

# 設定作者資料表在admin中相關操作
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('author_ch', 'author_fore')

# 設定譯者資料表在admin中相關操作
class TranslatorsAdmin(admin.ModelAdmin):
    list_display = ('translator_name',)

# Register your models here.
admin.site.register(Bookinfo, BookinfoAdmin)
admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Translators, TranslatorsAdmin)
