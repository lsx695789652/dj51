# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    return render(request, 'admin/login.html')
