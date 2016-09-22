# -*- coding: utf-8 -*-
from django.contrib.auth import login
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, TemplateView

from forms import UserRegisterForm, UserLoginForm


# 用户注册接口
class UserRegisterView(FormView):
    http_method_names = ['post']
    form_class = UserRegisterForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserRegisterView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        create_status, user_profile = form.save()
        if create_status is False:
            context = {
                'status': 'error',
                'msg': u'创建用户时出错, 请联系管理员!'
            }
        else:
            context = {
                'status': 'success',
                'msg': u'注册成功!用户编号是 {id}!'.format(id=user_profile.logic_id)
            }
        return JsonResponse(context)

    def form_invalid(self, form):
        context = {
            'status': 'error',
            'msg': form.errors.popitem()[-1][0]
        }
        return JsonResponse(context)


# 用户登陆接口
class UserLoginView(FormView):
    http_method_names = ['post']
    form_class = UserLoginForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserLoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user=user)
        return JsonResponse({
            'msg': u'登陆成功'
        })

    def form_invalid(self, form):
        context = {
            'status': 'error',
            'msg': form.errors.popitem()[-1][0]
        }
        return JsonResponse(context)


# 前端测试demo
class TemplateTestView(TemplateView):
    http_method_names = ['get']
    template_name = "500.html"

    def get_context_data(self, **kwargs):
        return {}
