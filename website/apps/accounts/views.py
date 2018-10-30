from rest_framework import views, permissions, status, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import JSONParser
from rest_framework.decorators import permission_classes

from .serializers import CommentsSerializer, BookshelfSerializer, UserSerializer
from .models import Comments, Bookshelf, User
import uuid


@permission_classes((AllowAny,))
class UserRegisterView(CreateAPIView):
    serializer_class = UserSerializer


class UserLogoutAllView(views.APIView):
    # Use this endpoint to log out all sessions for a given user.

    @permission_classes((IsAuthenticated,))
    def post(self, request, *args, **kwargs):
        user = request.user
        user.jwt_secret = uuid.uuid4()
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


@permission_classes((IsAuthenticated,))
class CommentsViewset(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    parser_classes = (JSONParser, )


@permission_classes((IsAuthenticated,))
class BookshelfViewset(viewsets.ModelViewSet):
    queryset = Bookshelf.objects.all()
    serializer_class = BookshelfSerializer
    parser_classes = (JSONParser, )
