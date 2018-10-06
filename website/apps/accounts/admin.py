from django.contrib import admin
from .models import Comments, Bookshelf, User


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('_id', 'comment_text', 'rating',
                    'read_status', 'created_time', 'user', 'bookinfo')
    search_fields = ('_id', 'read_status', 'created_time',)

class BookshelfAdmin(admin.ModelAdmin):
    list_display = ('_id', 'created_time', 'bookinfo', 'user')
    search_fields = ('_id', 'created_time',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'birthday', 'gender', 
    'location', 'is_active', 'is_staff')
    search_fields = ('username', 'email', 'birthday', 'gender',
                     'location', 'is_active', 'is_staff')


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Bookshelf, BookshelfAdmin)
