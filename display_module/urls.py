# -*- coding: utf-8 -*-

from django.conf.urls import url

from display_module import views

urlpatterns = [
    url(r'^user/register/$', views.UserRegisterView.as_view(), name='user_register'),
]
