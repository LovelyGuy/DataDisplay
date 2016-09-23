# -*- coding: utf-8 -*-

from django.views.generic import TemplateView


class Handle404View(TemplateView):
    http_method_names = ['get']

    def get_template_names(self):
        template_name = "500.html"
        return [template_name]

    def get_context_data(self, **kwargs):
        print "hello"


class Handle500View(TemplateView):
    http_method_names = ['get']

    def get_template_names(self):
        template_name = "500.html"
        return [template_name]
