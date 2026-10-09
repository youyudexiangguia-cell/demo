from django.shortcuts import render
from django.http import HttpResponse
from html import escape

# Create your views here.
def index(request):
    return HttpResponse("hello world")

def charpage(request):
    return HttpResponse("英文url页面")

def numpage(request):
    return HttpResponse("数字url页面")

def getData(request, urlData):
    return HttpResponse("get url " + urlData)

def getData2(request, d1, d2):
    return HttpResponse("get url: {} and url: {} ".format(d1, d2))

def getData3(request, data):
    s = "使用slug转换器， 数据为： %s， 类型为 %s"%(data, type(data))
    return HttpResponse(escape(s))
def getData4(request, data):
    s = "使用UUID转换器， 数据为： %s， 类型为 %s"%(data, type(data))
    return HttpResponse(escape(s))
def getData5(request, data):
    s = "使用path转换器， 数据为： %s， 类型为 %s"%(data, type(data))
    return HttpResponse(escape(s))

def getData6(request, data):
    return HttpResponse("数据: {}".format(data))

def getExtraData(request, data, ex): 
    return HttpResponse(\
        "get url and data1: {} and extra data2: {}".format(data, ex))

def useDefault(request, data = 123):
    return HttpResponse("参数是123，当前值：{}".format(data))

from django.urls import reverse

def getUrlNopara(request):
    return HttpResponse("url: {}".format(reverse("urlnopara")))
def geturlArgs(request, data):
    return HttpResponse("url: {}".format(reverse('urlargs', args = [data])))
def geturlKWArgs(request, data):
    return HttpResponse("url: {}".format(reverse('urlkwargs', kwargs = {"data": data})))
def getviewUrl(request):
    return HttpResponse("get view url: {}".format(reverse(geturlKWArgs, kwargs = {"data": 123})))
# 在模板中反向解析URL
def getTemp(request, data):
    # return render(request, "showurl.html, {}", {'data': data})
    return render(request, "showurl.html", {'data': data})