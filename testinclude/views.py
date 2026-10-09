from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def useinclude(request):
    return HttpResponse('这是useinclue view')

def ss(request):
    return HttpResponse('这是ss view')