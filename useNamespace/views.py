from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request, data = 0):
    return HttpResponse("默认页面url: {}, 获取数据的页面: {}"
                        .format(reverse("useNamespace:default"), 
                                reverse("useNamespace:ndata", args=[data])))