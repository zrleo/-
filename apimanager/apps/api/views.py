# -*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.


def list_views(request):
    return render(request, "list.html")


def edit_views(request):
    return render(request, "detail.html")
