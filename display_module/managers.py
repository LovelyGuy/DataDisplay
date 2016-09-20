# -*- coding: utf-8 -*-
from django.contrib.auth.base_user import BaseUserManager


# 用户创建的 manager
class UserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError(u'用户名不允许为空!')
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, email, **extra_fields):
        if not username:
            raise ValueError(u'用户名不允许为空!')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
