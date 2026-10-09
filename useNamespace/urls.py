# from django.contrib import admin
from django.urls import path
from . import views

app_name = "useNamespace"
urlpatterns = [
    path("", views.index, name = "default"),
    path("<data>/", views.index, name='ndata'),
]