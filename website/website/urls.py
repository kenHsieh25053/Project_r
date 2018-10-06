"""w URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
import debug_toolbar
from rest_framework import routers
from apps.books.views import BookinfoViewset, AuthorsViewset, TranslatorsViewset
from apps.accounts.views import CommentsViewset, BookshelfViewset
# from apps.accounts.views import UserLogoutAllView

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'bookinfo', BookinfoViewset)
router.register(r'authors', AuthorsViewset)
router.register(r'translators', TranslatorsViewset)
router.register(r'comments', CommentsViewset)
router.register(r'bookshelf', BookshelfViewset)


urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    re_path('auth/', include('apps.accounts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
]
