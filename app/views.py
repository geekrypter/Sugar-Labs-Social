# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.response import TemplateResponse
from django.shortcuts import render

def index(request):
    return TemplateResponse(request, 'skeleton/base.html',)
