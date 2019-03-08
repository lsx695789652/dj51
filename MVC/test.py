# coding:utf-8
from MVC.ClassLib.urldata import reqdata
from django.http import HttpResponse


def test(request):
    req = reqdata()
    url = "http://www.baidu.com"
    res = req.requrl(url)
    print(res)

