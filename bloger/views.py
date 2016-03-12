# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from bloger.models import Article
from datetime import datetime

# Create your views here.


# def home(request):
#     return HttpResponse("Hello world,Django")


# def details(request, my_args):
#     return HttpResponse("You are looking at my_args %s." % my_args)
#     post = Article.objects.all()[int(my_args)]
#     post = Article.objects.filter(id=int(my_args))
#     post = Article.objects.get(id=int(my_args))
#     str = ("title = %s, category = %s, date_time = %s, content = %s"
#            % (post.title, post.category, post.date_time, post.content))
#     return HttpResponse(str)

def test(request):
    return render(request, 'test.html', {'current_time':datetime.now()})


def home(request):
    post_list = Article.objects.all() #获取Article全部对象
    return render(request, 'home.html', {'post_list':post_list})

def details(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post':post})
