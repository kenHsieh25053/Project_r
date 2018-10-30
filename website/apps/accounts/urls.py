from django.urls import re_path
import djoser.views as djoser_views
import rest_framework_jwt.views as jwt_views
from .views import UserLogoutAllView, UserRegisterView


app_name = 'accounts'

urlpatterns = [
    # Views are defined in Djoser, but we're assigning custom paths.
    re_path('user/view/', djoser_views.UserView.as_view(), name='user-view'),
    re_path('user/delete/', djoser_views.UserDeleteView.as_view(),
            name='user-delete'),
    # need to create custom view
    #     re_path('user/create/', djoser_views.UserCreateView.as_view(),
    #             name='user-create'),
    re_path('user/create/', UserRegisterView.as_view(),
            name='user-create'),
    # Views are defined in Rest Framework JWT, but we're assigning custom paths.
    re_path('user/login/', jwt_views.ObtainJSONWebToken.as_view(),
            name='user-login'),
    re_path('user/login/refresh/',
            jwt_views.RefreshJSONWebToken.as_view(), name='user-login-refresh'),
    re_path('user/logout/all/', UserLogoutAllView.as_view(),
            name='user-logout-all')
]
