import uuid
from rest_framework import views, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import CommentsSerializer, BookshelfSerializer
from .models import Comments, Bookshelf, User


class UserLogoutAllView(views.APIView):
    # Use this endpoint to log out all sessions for a given user.
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        user.jwt_secret = uuid.uuid4()
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentsViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class BookshelfViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Bookshelf.objects.all()
    serializer_class = BookshelfSerializer
