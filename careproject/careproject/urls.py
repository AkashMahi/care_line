"""
URL configuration for careproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from careapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index),
    path("abt",about),
    path('care_reg/',caretaker_registration),
    path('client_reg/',client_reg),
    path('cms_dash/',cms_dash),
    path('rec_request/',rec_request),
    path('approvecr/<int:id>',apprv_cr),
    path('reject/<int:id>',reject),
    path('rejectmsg/<int:id>',rejectmsg),
    path('sup/',support),
    path("vsup/",view_support),
    path('care_dash/',care_dash),
    path('lgin/',logins),
    path('lgout/',logouts),
]
