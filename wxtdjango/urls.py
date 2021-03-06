"""wxtdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from wxtdemo.views import show_atis, show_page, show_search, DepartmentList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_page, name="home-en"),
    path('en', show_page, name="home-en"),
    path('ati', show_atis),
    path('departments', DepartmentList.as_view()),
    path('search', show_search)
]

from django.conf import settings
from django.conf.urls import include, url

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
