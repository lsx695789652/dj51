# _*_ coding : utf-8 _*_
from django.shortcuts import render_to_response


def main(request):
    return render_to_response('main.html')


def left(request):
    return render_to_response('left.html')


def head(request):
    return render_to_response('head.html')


def foot(request):
    return render_to_response('footer.html')
