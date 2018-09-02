# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from users.views import Check_Login

@Check_Login
def index(request):
	return render(request,'index.html',{'aopen':1})


	
