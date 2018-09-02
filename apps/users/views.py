# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login ,logout
from django.http import HttpResponseRedirect

def Check_Login(func):  #自定义登录验证装饰器
	def warpper(request):
		username = request.session.get('username')
		if username:
			return func(request)
		else:
			return render(request,'users/login.html')
	return warpper

def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)	
		if user is not None:			
			login(request, user)
			# Redirect to a success page.
			request.session['username'] = user.username			
			return render(request,'index.html',{'username': username})
		else:
			# Return an error message.
			error = '用户名或密码错误'
			return render(request, 'users/login.html', {'error': error})


def logout_view(request):	
	logout(request)
	username = request.session.get('username')
	if username:
		del request.session["username"]  # 删除session
	# Redirect to a success page.
	return render(request,'users/login.html')