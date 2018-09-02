# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from users.views import Check_Login
# Create your views here.

@Check_Login
def manual(request):
	return render(request,'other/manual.html')
