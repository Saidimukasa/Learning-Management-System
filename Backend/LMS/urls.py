"""LMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.contrib.auth.views import (PasswordResetView,
 PasswordResetDoneView,
 PasswordResetConfirmView,
 PasswordChangeDoneView
 )
from django.contrib.auth.views import LogoutView
from .constants import *
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = SCHOOL_NAME + " Admin"
admin.site.site_title = SCHOOL_NAME + " Admin Portal"
admin.site.index_title = "Welcome to " + SCHOOL_NAME + " Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/',views.signin,name='signin'),
    path('student/', include('student.urls')),
    path('change-password/',views.PasswordChangeManager.as_view(),name='password_change'),
]

if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)