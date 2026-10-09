"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin    
from django.urls import path, re_path, include
from first import views
# from testinclude import views as tv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    # re_path(r'^[A-Za-z]+$', views.charpage),
    # re_path(r'^\d{2,}$', views.numpage),
    # path("include/", tv.useinclude),
    # path("root/", include("testinclude.urls")),
    # path("test/<urlData>/", views.getData),
    # path("test/<d1>/<d2>/", views.getData2),
    # path("test/<str:d1>/<int:d2>/", views.getData2),
    # path("data3/<slug:data>", views.getData3),
    # path("data4/<uuid:data>", views.getData4),
    # path("data5/<path:data>", views.getData5),
    re_path(r'^reex/(?P<data>[a-z0-9]+)$', views.getData6),
    path("extra/<data>", views.getExtraData, {'ex':"123"}),
    path("default/", views.useDefault),
    path("default/<data>/", views.useDefault),
    path("rev/abc", views.getUrlNopara, name = "urlnopara"),
    path("rev2/<data>", views.geturlArgs, name = 'urlargs'),
    path("rev3/<data>", views.geturlKWArgs, name = 'urlkwargs'),
    path("rev4/view", views.getviewUrl),
    path("uset/<data>", views.getTemp, name = 'urlTemplate'),
    path('usename1/', include('useNamespace.urls')),
    path('usenames/', include('useNamespace.urls')),
]
