# -*- coding: utf-8 -*-
from django import forms
from django.db import transaction

from display_module.models import UserModel


# 用户注册表单
class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=32, required=True, label=u'用户名')
    email = forms.EmailField(required=True, label=u'邮箱', widget=forms.EmailInput(),
                             error_messages={
                                 'required': u'邮箱为空',
                                 'invalid': u'邮箱格式错误'
                             })
    password = forms.CharField(label=u'密码', min_length=6,
                               widget=forms.PasswordInput(), required=True,
                               error_messages={
                                   'required': u'密码为空!',
                                   'invalid': u'密码长度不够!',
                               })
    password_repeat = forms.CharField(label=u'第二次密码', min_length=6,
                                      widget=forms.PasswordInput(), required=True,
                                      error_messages={
                                          'required': u'重复输入的密码为空!',
                                          'invalid': u'重复输入的密码长度不够!',
                                      })

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            UserModel.objects.get(username=username)
        except:
            return username
        else:
            raise forms.ValidationError(u'该用户名已被注册!')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            user = UserModel.objects.get(email=email)
            username = user.username
        except:
            return email
        else:
            err_msg = u'改邮箱已经注册了用户名为"{username}"的账户.'.format(username=username)
            raise forms.ValidationError(err_msg)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError(u'密码为空')
        return password

    def clean(self):
        password = self.cleaned_data.get('password')
        password_repeat = self.cleaned_data.get('password_repeat')
        if password != password_repeat:
            raise forms.ValidationError(u'两次输入的密码不一致!')
        return self.cleaned_data

    @transaction.atomic()
    def save(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        email = self.cleaned_data.get('email')
        try:
            user = UserModel.objects.create_user(username=username, email=email, password=password)
        except Exception as e:
            print e
            return False, None
        else:
            return True, user


# TODO: 待实现
class UserLoginForm(forms.Form):
    username = forms.CharField()
