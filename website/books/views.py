from .models import Bookinfo, Authors, Translators
from .serializers import BookinfoSerializer, AuthorsSerializer, TranslatorsSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

# 書籍資料API，以json格式傳遞到前端
class BookinfoViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Bookinfo.objects.all()
    serializer_class = BookinfoSerializer

# 作者資料API，以json格式傳遞到前端
class AuthorsViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer

# 譯者資料API，以json格式傳遞到前端
class TranslatorsViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Translators.objects.all()
    serializer_class = TranslatorsSerializer

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
