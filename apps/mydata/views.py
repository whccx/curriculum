# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView
from mydata import models 
from setrule.models import Makebaseclass
#-------------------------------
from django.utils.decorators import method_decorator
from users.views import Check_Login


#===========================================
@method_decorator(Check_Login,name='dispatch') 
class Show(ListView):	
	model = models.Department

#===========================================
@method_decorator(Check_Login,name='dispatch')
class Show_myclass(View):
	template_name = 'mydata/myclass.html'		
	#-------------------------------
	def get(self,request):
		if request.method == 'GET':
			show_myclass_list = models.Myclass.objects.all()
			return render(request,self.template_name,{'show_myclass_list':show_myclass_list})
	#-------------------------------
	def post(self,request):
		if request.method == 'POST':
			if request.POST.get('restart','')=='true':
				restart(request)
		show_myclass_list = models.Myclass.objects.all()
		return render(request,self.template_name,{'show_myclass_list':show_myclass_list})

#-------------------------------
def restart(request):	
	models.Myclass.objects.all().delete()
	show_grade_list = models.Grade.objects.all()
	myid=1
	for gline in show_grade_list:		
		for i in range(1,int(gline.class_num)+1):
			myclass_name_temp = gline.year+ '级' + gline.g_pf_name + str(i) + '班'
			c_num = Makebaseclass.objects.filter(id=myid).first()
			models.Myclass.objects.create(
				id=myid,
				myclass_name=myclass_name_temp,
				m_grade_name=gline.grade_name,
				m_pf_name=gline.g_pf_name,
				myclass_num=c_num.baseclass_stunum,
				)
			myid += 1
#===========================================
