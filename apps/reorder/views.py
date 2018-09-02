# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from reorder import models
from users.views import Check_Login
from setrule.models import Makebaseclass,Maketeachsm
from random import choice

@Check_Login
def start(request):
	subject_list = models.Subjectall.objects.filter(id=1)
	#-------------
	if subject_list.exists()==False:
		basedic=add_data()
	#-----------------------------------
	subject_list = models.Subjectall.objects.all()
	classnum_list = models.Subjectall.objects.values('classnum').distinct()
	#-----------------------------------
	if request.method == 'POST':
		if request.POST.get('baselist')=='true':
			models.Subjectall.objects.all().delete()
			basedic=add_data()
			subject_list = models.Subjectall.objects.all()
		#-----------------------------------
		if request.POST.get('create_pt_subject')=='true':	
			print pt_rule(classnum_list)
		#-----------------------------------
	return render(request,'reorder/start.html',{
		'subject_list':subject_list,
		'classnum_list':classnum_list,
		})

#==========================================================
def add_data():
	basedic=[]
	a=0
	maxclassnum=Makebaseclass.objects.latest('id').id
	for i in range(1, maxclassnum+1):
		for ii in range(1, 6):
			models.Subjectall.objects.create(
				id=a+1,
				classnum=i,
				week=ii,
				one=i*100+ii*10+1,
				two=i*100+ii*10+2,
				three=i*100+ii*10+3,
				)
			a=a+1
			basedic.append(i*100+ii*10+1)
			basedic.append(i*100+ii*10+2)
			basedic.append(i*100+ii*10+3)
	return(basedic)
#==========================================================
# from django.db.models import Q
# models.Subjectall.objects.filter(Q(classnum=2)&Q(week=4)).update(two=242)
# meget = models.Subjectall.objects.get(classnum=2,week=4).two
# print(meget)
def pt_rule(classnum_list):
	templist=[]		
	testlist=[]
	oklist=[]
	for i in range(1,len(classnum_list)+1):
		testlist.append(i)
	#-----------------
	pt_list=Maketeachsm.objects.filter(teacher_type='兼职')			
	for pt in pt_list:						
		if pt.must_time !='':
			ptlist=pt.must_time.split(",")
			temp_testlist=testlist
			for i in ptlist:
				ran = choice(temp_testlist)
				templist.append(int(i))
				oklist.append(ran*100+int(i))
	#-----------------
	if len(classnum_list)<len(pt_list):
		from collections import Counter
		if max(Counter(templist).values())>len(classnum_list):
			print('error')
	return(oklist)