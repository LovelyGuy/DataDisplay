# -*- coding: utf-8 -*-
from django.contrib.auth.base_user import BaseUserManager


# 用户创建的 manager
class UserManager(BaseUserManager):
    def create_user(self, user, logic_id, **extra_fields):
        """
        创建普通用户
        :param user:    User object
        :param logic_id:    逻辑主键
        :param extra_fields:    extra params
        :return:    user_profile
        """
        if not user:
            raise ValueError(u'用户为空!')
        try:
            user = self.model.get(logic_id=logic_id)
        except Exception as e:
            print e
            user_profile = self.model(user=user, logic_id=logic_id, **extra_fields)
            user_profile.save()
            return user_profile
        else:
            err_message = u"用户逻辑主键重复!"
            raise ValueError(err_message)

    def create_superuser(self, user, logic_id, **extra_fields):
        """
        创建超级用户
        :param user:    User object
        :param logic_id:    逻辑主键
        :param extra_fields:    extra params
        :return:    user_profile
        """
        if not user:
            raise ValueError(u'用户为空!')
        user_profile = self.model(user=user, logic_id=logic_id, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user_profile
