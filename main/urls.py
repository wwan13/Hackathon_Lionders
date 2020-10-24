"""Lionders URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('on_going',views.on_going,name='on_going'),
    path('detail',views.detail,name='detail'),
    path('require_login',views.require_login,name='require_login'),
    path('create_objs',views.create_objs,name='create_objs'),
    path('create_item_objects',views.create_item_objects,name="create_item_objects"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
