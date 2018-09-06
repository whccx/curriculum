# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from reorder import models
from setrule import models as sr
from mydata import models as md
from collections import Counter
from random import choice
from users.views import Check_Login

@Check_Login
def start(request):	
	ms=models.Subjectall.objects
	subject_list = ms.filter(id=1)
	#-------------
	if subject_list.exists()==False:
		basedic=add_data()
	#-----------------------------------
	subject_list = ms.all()
	classnum_list = ms.values('classnum').distinct()
	#-----------------------------------
	if request.method == 'POST':
		rp=request.POST
		if rp.get('baselist')=='true':
			ms.all().delete()
			basedic=add_data()
			subject_list = ms.all()
		#-----------------------------------
		if rp.get('create_pt_subject')=='true':	
			pt_rule(classnum_list)
		#-----------------------------------
	return render(request,'reorder/start.html',{
		'subject_list':subject_list,
		'classnum_list':classnum_list,
		})

#==========================================================
def add_data():
	basedic=[]
	a=0
	maxclassnum=sr.Makebaseclass.objects.latest('id').id
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
def pt_rule(classnum_list):
	okgood=0
	while okgood==0:
		mplist=[]
		stlist=[]
		oklist=[]
		classn=[]
		bblist=[]
		teacher_dic={}
		for i in range(1,len(classnum_list)+1):
			stlist.append(i)
		#print stlist
		#-----------------
		ran=0
		pt_list=sr.Maketeachsm.objects.filter(teacher_type='兼职')
		for pt in pt_list:
			mp_st=stlist
			if pt.must_time !='':
				ran = choice(mp_st)
				ptlist=pt.must_time.split(",")			
				#print pt.max_classes
				testone=mtms(pt,ran,pt.profess_subject,1)		
				while testone==False:				
					mp_st.remove(ran)
					ran = choice(mp_st)
					if int(ran)>0:
				 		testone=mtms(pt,ran,pt.profess_subject,1)
				 		
				 	else:
				 		print('god')
				 		break
				#testtwo=mtms(pt,ran,pt.public_subject,2)
				#stlist.remove(ran)
				for i in ptlist:
					mplist.append(int(i))
					oklist.append(ran*100+int(i))

				if max(Counter(mplist).values())>len(classnum_list):
					print('同样的必排时间数量大于班级数量')
					break
				teacher_dic[pt.teacher_name]=oklist			
				bblist+=oklist
				oklist=[]			
				classn.append(ran)
			#-----------------
		
		if len(bblist)==len(set(bblist)):
			if len(classn)==len(set(classn)):
				okgood=1
				print('课程没有冲突')
	print teacher_dic
	

#==========================================================
def mtms(me,ran,subject,stype):
	err=True
	dd=sr.Makebaseclass.objects.get(id=ran)	
	ee=sr.Makegradetp.objects.filter(
		depart=dd.basedepart_name,
		grade=dd.basegrade_name,
		profess=dd.baseprofess_name
		)	
	if len(subject)>0:
		bbb=0
		sl=subject.split(",")
		for s in sl:								
			if stype==1:
				ps=md.Profess_subjects.objects.get(id=int(s))					
				for e in ee:
					if e.subject_name==ps.ms_name:
						ww=int(e.theory_classes)+int(e.practice_classes)
						if ww>me.max_classes:
							err=False
						else:
							bbb=1
							print(me.teacher_name+':'+e.subject_name+str(ww))	
						break

			if stype==2:
				ps=md.Public_subjects.objects.get(id=int(s))
				for e in ee:
					if e.subject_name==ps.ps_name:
						bbb=1
						ww=int(e.theory_classes)+int(e.practice_classes)			
						print(me.teacher_name+':'+e.subject_name+str(ww))
			import time
			time.sleep(0);
		if bbb==0:
			err=False
	return(err)			
	#Makebaseclass mteacher_name msubject
	#Maketeachsm profess_subject public_subject

