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
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('login_fail/',views.login_fail,name='login_fail'),
    path('signup_consumer/',views.signup_consumer,name='signup_consumer'),
    path('signup_lionders/',views.signup_lionders,name='signup_lionders'),
    path('usertype/',views.usertype,name='usertype'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('mypage/',views.mypage,name='mypage'),
    path('update_user_info/',views.update_user_info,name='update_user_info'),
    path('education/',views.education,name='education'),
]
