"""website URL Configuration

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
from django.urls import include, path
from django.conf import settings
import debug_toolbar
from django.contrib.auth.models import User
from rest_framework import routers
from books.views import BookinfoViewset, AuthorsViewset, TranslatorsViewset, UserViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'bookinfo', BookinfoViewset)
router.register(r'authors', AuthorsViewset)
router.register(r'translators', TranslatorsViewset)

urlpatterns = [
    path(r'__debug__/', include(debug_toolbar.urls)),
    # path(r'docs/', include('rest_framework_docs.urls')),
    path(r'', include(router.urls)),
    path(r'api-auth/', include('rest_framework.urls')),
    path(r'accounts/', include('allauth.urls')),
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/', admin.site.urls),
]
