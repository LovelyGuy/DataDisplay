# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import transaction

from display_module.models.models import UserProfile
from utils.generator_util import get_uuid


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
            User.objects.get(username=username)
        except Exception as e:
            print e
            return username
        else:
            raise forms.ValidationError(u'该用户名已被注册!')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            user = User.objects.get(email=email)
            username = user.username
        except Exception as e:
            print e
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
        user_id = get_uuid()
        try:
            user = User(username=username, password=password, email=email)
            user.set_password(password)
            user.save()
            user_profile = UserProfile.objects.create_user(user=user, logic_id=user_id)
        except Exception as e:
            print e
            return False, None
        else:
            return True, user_profile


# 用户登陆表单
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=32, required=False)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput(), required=True,
                               error_messages={
                                   'required': u'密码为空',
                                   'invalid': u'密码错误',
                               })

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            try:
                User.objects.get(username=username)
            except:
                raise forms.ValidationError(u'用户名不存在')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            try:
                User.objects.get(email=email)
            except:
                raise forms.ValidationError(u'该邮箱未注册')
        return email

    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        data = {
            'password': password
        }
        if username:
            data.update({
                'username': username,
            })
        if email:
            data.update({
                'email': email,
            })
        user = authenticate(username=username, password=password)
        if user:
            self.user = user
        return self.cleaned_data

    def get_user(self):
        return self.user
