# _*_ coding : utf-8 _*_
from django.http import HttpResponse
from MVC.Models import User
from django.shortcuts import render, render_to_response
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json


def index(request):
    # user = User(name='test')
    # user.save()
    # return HttpResponse("<p>数据添加成功</p>")
    output = _("Welcome to my site.")
    list = User.objects.all().order_by("id")
    data = {}
    province = serializers.serialize("json" , list)
    data["ctx"] = json.loads(province)
    return render(request, "index.html", data)


@csrf_exempt
def save(request):
    if request.POST:
        user = User(name=request.POST['username'])
        user.save()
    list = User.objects.all().order_by("id")
    data = {}
    province = serializers.serialize("json", list)
    data["ctx"] = json.loads(province)
    return render(request, "index.html", data)


def userDetail():
    result = ""
    # 相当于select* from table
    lists = User.objects.all()
    # 过滤条件查询
    response = User.objects.filter(id=1)
    # 查询单条记录
    response1 = User.objects.get(id=1)
    # 限制返回条数
    User.objects.order_by("name")[0:2]
    # 数据排序
    User.objects.order_by("id")
    # 多条连续使用
    User.objects.filter(name='test').order_by('id')
    # 输出所有数据
    for var in lists:
        result += var.name+','

    # 修改数据
    test = User.objects.get(id=1)
    test.name = 'ceshi1'
    test.save()
    # 删除数据
    test1 = User.objects.get(id=1)
    test1.delete()
    return HttpResponse("<p>数据添加成功"+result+"</p>")
