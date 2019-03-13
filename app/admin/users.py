# _*_ coding : utf-8 _*_
from django.http import HttpResponse
from django.http import JsonResponse
from app.models import User
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
    province = serializers.serialize("json", list)
    data["ctx"] = json.loads(province)
    return render(request, "admin/UserManage/index.html", data)


@csrf_exempt
def save(request):
    data = {}
    result = saveuser(request)
    txt = ''
    if result == 101:
        txt = '用户已存在'
    elif result == 200:
        txt = '创建成功'
    elif result == 400:
        txt = '没接收到数据'
    else:
        txt = '运行出错'
    data['txt'] = txt
    return render(request, "admin/UserManage/index.html", data)


def saveuser(request):
    try:
        if request.POST:
            old = User.objects.filter(name=request.POST['username'])
            if old:
                return 101
            user = User(name=request.POST['username'], password=request.POST['password'])
            user.save()
            return 200
        return 404
    except Exception as e:
        return 500


def update(request):
    return render_to_response('admin/UserManage/index.html')


def delete(request):
    return render_to_response('admin/UserManage/index.html')


def detail(request):
    data = {}
    id = ''
    if request.GET:
        id = request.GET['id']
    data['id'] = id
    return render(request, 'admin/UserManage/detail.html', data)


@csrf_exempt
def selectdata(request):
    if request.GET:
        page = request.GET["page"]
        limit = request.GET["limit"]
    userlist = User.objects.all().values()
    data = {}
    # province = serializers.serialize("json", userlist)
    # data["ctx"] = json.loads(province)
    data["code"] = 0
    data["msg"] = request.GET["page"]
    data["count"] = userlist.count()
    data["data"] = list(userlist)

    return JsonResponse(data, safe=False)


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
        result += var.name + ','

    # 修改数据
    test = User.objects.get(id=1)
    test.name = 'ceshi1'
    test.save()
    # 删除数据
    test1 = User.objects.get(id=1)
    test1.delete()
    return HttpResponse("<p>数据添加成功" + result + "</p>")
