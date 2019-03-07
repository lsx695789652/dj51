# _*_ coding : utf-8 _*_
from django.shortcuts import render_to_response


def main(request):
    return render_to_response('admin/main.html')


def left(request):
    return render_to_response('admin/left.html')


def head(request):
    return render_to_response('admin/head.html')


def foot(request):
    return render_to_response('admin/footer.html')
