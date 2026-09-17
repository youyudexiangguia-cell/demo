from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello world")

def charpage(request):
    return HttpResponse("英文url页面")

def numpage(request):
    return HttpResponse("数字url页面")