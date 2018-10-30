from rest_framework import serializers
from .models import Comments, Bookshelf, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'password',
                  'user_image',
                  'birthday',
                  'gender',
                  'location',
                  'about')


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('_id',
                  'comment_text',
                  'rating',
                  'read_status',
                  'created_time',
                  'user',
                  'bookinfo')


class BookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookshelf
        fields = ('_id',
                  'created_time',
                  'updated_at',
                  'bookinfo',
                  'user')
