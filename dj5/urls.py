"""webdig URL Configuration

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
from django.urls import path
import app.users as use
import app.layout as lay
import app.tests as test



urlpatterns = [
    path('admin/', admin.site.urls),
    path('tests/', test.test),
    path('index/', lay.main),
    path('left/', lay.left),
    path('user/', use.index),
    path('save', use.save),
    path('select/', use.selectdata),
    path('detail/', use.detail)

]
