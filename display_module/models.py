# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser, User
from django.db import models

from display_module.managers import UserManager


# 用户信息表
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    logic_id = models.CharField(max_length=32, db_index=True, verbose_name=u'用户的逻辑主键')
    gender = models.NullBooleanField(null=True, verbose_name=u'性别')
    city = models.CharField(max_length=32, blank=True, null=True, verbose_name=u'所在城市')
    join_time = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=u'注册时间')

    objects = UserManager()
    USERNAME_FIELD = 'username'

    class Meta(AbstractUser.Meta):
        db_table = 'user_profile'
        verbose_name = u'用户信息表'

    def get_short_name(self):
        return "数源用户: {username}".format(username=self.username)

    def get_full_name(self):
        return "{username}: {email}".format(username=self.username, email=self.email)
