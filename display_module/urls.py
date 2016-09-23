# -*- coding: utf-8 -*-

from django.conf.urls import url

from display_module.views import views

urlpatterns = [
    url(r'^user/register/$', views.UserRegisterView.as_view(), name='user_register'),
    url(r'^user/login/$', views.UserLoginView.as_view(), name='user_login'),
]
