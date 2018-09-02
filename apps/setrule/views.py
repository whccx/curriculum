# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect

import json

from setrule import models
from mydata.models import Myclass,Grade,Professional,Schoolplace,Public_subjects
from mydata.models import Profess_subjects,Fulltimeteacher,Parttimeteacher,Substituteteacher
#--------------------------------------------------------------------
from users.views import Check_Login

@Check_Login	
def sindex(request):		
	show_mbc_list = models.Makebaseclass.objects.all()
	if show_mbc_list.exists()==False:
		create_mbc()
	Dics = []
	for md in show_mbc_list:
		dic_ccx = {
			"id": md.id,
			"stock": md.baseclass_name,
			"name": md.basegrade_name,
			"sdate" : md.baseclass_year,
			"ship" : md.baseclass_num,
			"note1" : md.baseprofess_name,
			"note2" : md.basedepart_name,
			"note3" : md.schoolplace_class,
			"note4" : md.baseclass_stunum,
			"note5" : md.mteacher_name,
			"note6" : md.msubject,
		}		
		Dics.append(dic_ccx)
	#------------------
	sp=Schoolplace.objects.all()
	mylist=stradd(sp,'schoolplace_num')
	#------------------
	ep = Profess_subjects.objects.all()
	ep_dic=stradd(ep,'ms_name')
	#------------------	
	fl=models.Maketeachsm.objects.filter(teacher_type='全职')
	ft_list=stradd(fl,'teacher_name')
	#------------------
	return render(request,'setrule/sindex.html',{
		'Dics':json.dumps(Dics),
		'mylist':mylist,
		'ep_dic':ep_dic,
		'ft_list':ft_list,
		})
	#------------------
def stradd(ep,f): # 参数f是参数ep里面的key,表里的字段名
	mstr=''	
	i=1
	for p in ep:
		e=getattr(p,f)     #= p.f
		if i==len(ep):
			mstr=mstr+e+str(":")+e
		else:
			mstr=mstr+e+str(":")+e+str(";")
		i+=1
	return mstr

def create_mbc():
	smclists = Myclass.objects.all()	
	for sl in smclists:
		pflist=Professional.objects.get(pf_name=sl.m_pf_name)
		glist=Grade.objects.get(grade_name=sl.m_grade_name,g_pf_name=sl.m_pf_name)
		models.Makebaseclass.objects.create(
			id=sl.id,
			baseclass_name=sl.myclass_name,
			basegrade_name=sl.m_grade_name,
			baseprofess_name=sl.m_pf_name,
			basedepart_name=pflist.dp_name,
			baseclass_year=glist.year,
			baseclass_num=glist.class_num,
			schoolplace_class="301",
			baseclass_stunum=sl.myclass_num,
			mteacher_name='tc',
			msubject='mc',
			)
	
#--------------------------------------------------------------------
@Check_Login
def m_tsm(request):	
	#---------
	teach_base_parttime = Parttimeteacher.objects.all()
	for tbp in teach_base_parttime:
		mbc_tn=models.Maketeachsm.objects.filter(teacher_name=tbp.pt_name)
		if mbc_tn.exists()==False:
			mt_id=models.Maketeachsm.objects.all()
			if mt_id.exists()==False:
				mbc_id=1
			else:
				mbc_id=int(models.Maketeachsm.objects.latest('id').id)+1
			models.Maketeachsm.objects.create(teacher_name=tbp.pt_name,id=mbc_id,teacher_type='兼职')
	#---------
	teach_base_fulltime = Fulltimeteacher.objects.all()
	for tbf in teach_base_fulltime:
		mbc_tn=models.Maketeachsm.objects.filter(teacher_name=tbf.ft_name)
		if mbc_tn.exists()==False:
			mbc_id=int(models.Maketeachsm.objects.latest('id').id)+1
			models.Maketeachsm.objects.create(teacher_name=tbf.ft_name,id=mbc_id,teacher_type='全职')
	#---------
	teach_base_substitute = Substituteteacher.objects.all()
	for tbs in teach_base_substitute:
		mbc_tn=models.Maketeachsm.objects.filter(teacher_name=tbs.st_name)
		if mbc_tn.exists()==False:
			mbc_id=int(models.Maketeachsm.objects.latest('id').id)+1
			models.Maketeachsm.objects.create(teacher_name=tbs.st_name,id=mbc_id,teacher_type='代课')
	#-------------------------------------
	#teach subject and time
	Subject_public_dics={}
	show_ps_list = Public_subjects.objects.all()
	for ps_dic in show_ps_list:
		Subject_public_dics[ps_dic.id] = ps_dic.ps_name

	Subject_profess_dics={}
	show_ms_list = Profess_subjects.objects.all()
	for ms_dic in show_ms_list:
		Subject_profess_dics[ms_dic.id] = ms_dic.ms_name

	if request.method == 'POST':		
		my_teacher_name=request.POST.get('my_teacher_name','')
		maxme = request.POST.get('spinner1','')
		minme = request.POST.get('spinner2','')
		c_profess = request.POST.get('profess','')
		c_public = request.POST.get('public','')
		c_mtime = request.POST.get('mtime','')
		c_untime = request.POST.get('untime','')
		c_radio = request.POST.get('form-field-radio','')
		c_duallistbox = request.POST.getlist('duallistbox1')
		myduallist = ""
		for i in range(len(c_duallistbox)):			
			if i==0:
				myduallist = str(c_duallistbox[i])
			else:
				myduallist = myduallist + ',' + str(c_duallistbox[i])
		if c_radio=="1":
			c_profess = myduallist
		if c_radio=="2":
			c_public = myduallist
		if c_radio=="3":
			c_mtime = myduallist
		if c_radio=="4":
			c_untime = myduallist
		models.Maketeachsm.objects.filter(id=my_teacher_name).update(
			profess_subject=c_profess,
			public_subject=c_public,
			max_classes=maxme,
			min_classes=minme,
			must_time=c_mtime,
			unable_time=c_untime,
			)
		
	show_mbc_list = models.Maketeachsm.objects.all()
	#data dics
	Dics = []
	for mbc_dic in show_mbc_list:
		dic_ccx = {
		"id": mbc_dic.id,
		"teacher_name": mbc_dic.teacher_name,
		"teacher_type": mbc_dic.teacher_type,
		"public_subject" : mbc_dic.public_subject,
		"profess_subject" : mbc_dic.profess_subject,
		"max_classes" : mbc_dic.max_classes,
		"min_classes" : mbc_dic.min_classes,
		"must_time" : mbc_dic.must_time,
		"unable_time" : mbc_dic.unable_time
		}		
		Dics.append(dic_ccx)

	return render(
			request,'setrule/m_tsm.html',
			{
			'Subject_public_dics':json.dumps(Subject_public_dics),
			'Subject_profess_dics':json.dumps(Subject_profess_dics),
			'Dics':json.dumps(Dics),				
			'weekclasses':json.dumps(weekclasses),
			},
			)

#--------------------------------------------------------------------	
@Check_Login
def m_gtp(request):
	select_depart=""
	select_profess=""
	select_grade=""

	show_mbc_list = models.Makebaseclass.objects.all()
	all_grade=[]
	all_profess=[]
	all_depart=[]

	for mbc_dic in show_mbc_list:
		#
		if mbc_dic.basegrade_name not in all_grade:
			all_grade.append(mbc_dic.basegrade_name)
		#
		if mbc_dic.baseprofess_name not in all_profess:
			all_profess.append(mbc_dic.baseprofess_name)
		#
		if mbc_dic.basedepart_name not in all_depart:
			all_depart.append(mbc_dic.basedepart_name)		
	if select_grade=="":
		select_grade=all_grade[0]
	if select_profess=="":
		select_profess=all_profess[0]
	if select_depart=="":
		select_depart=all_depart[0]

	#----------------------------
	edit_public=[]
	edit_profess=[]

	edit_publics = Public_subjects.objects.all()
	for epb in edit_publics:
		edit_public.append(epb.ps_name)

	edit_professs = Profess_subjects.objects.all()
	for epf in edit_professs:
		edit_profess.append(epf.ms_name)

	#----------------------------

	if request.method == 'POST':
		#print request.body
		myid=request.POST.get('id','0')
		my_subject_name=request.POST.get('subject_name','')
		my_theory_classes=int(request.POST.get('theory_classes','0'))
		my_practice_classes=int(request.POST.get('practice_classes','0'))
		my_prior_order=int(request.POST.get('prior_order','0'))
		my_cha=request.POST.get('oper','')
		if my_cha=="edit":
			edit_subject_type=request.POST.get('subject_type','')
			models.Makegradetp.objects.filter(id=myid).update(
				subject_name=my_subject_name,
				theory_classes=my_theory_classes,
				practice_classes=my_practice_classes,
				prior_order=my_prior_order,
				subject_type=edit_subject_type,
				)
		if my_cha=="del":
			models.Makegradetp.objects.filter(id=myid).delete()
		if my_cha=="add":
			add_grade=request.POST.get('grade','')
			add_profess=request.POST.get('profess','')
			add_depart=request.POST.get('depart','')
			add_subject_type=request.POST.get('subject_type','')
			show_mbc_list = models.Makegradetp.objects.all()
			meid=0
			for mbc_dic in show_mbc_list:
				if mbc_dic.id>meid:
					lsid=mbc_dic.id
					if lsid-meid>1:
						break						
					else:
						meid=mbc_dic.id
			models.Makegradetp.objects.create(
				id=meid+1,
				subject_name=my_subject_name,
				theory_classes=my_theory_classes,
				practice_classes=my_practice_classes,
				prior_order=my_prior_order,
				grade=add_grade,
				profess=add_profess,
				depart=add_depart,
				subject_type=add_subject_type,
				)
		if my_cha=="my_search":
			select_depart=request.POST.get('select1','0')
			select_profess=request.POST.get('select2','0')
			select_grade=request.POST.get('select3','0')
			
	#------------------------------------------
	show_gtp_list =models.Makegradetp.objects.filter(depart=select_depart,profess=select_profess,grade=select_grade)	
	myrows=[]
	myrowsone=[]
	mycellone=[]
	Dics={}
	total_theory_classes=0
	total_practice_classes=0
	total_classes=0
	
	#-----------
	for mbc_dic in show_gtp_list:
		mycellone=[
			mbc_dic.id,
			mbc_dic.subject_type,
			mbc_dic.subject_name,			
			mbc_dic.theory_classes,			
			mbc_dic.practice_classes,
			mbc_dic.prior_order,			
			mbc_dic.grade,
			mbc_dic.profess,
			mbc_dic.depart
		]
		myrowsone={"id":str(mbc_dic.id),"cell":mycellone}
		myrows.append(myrowsone)
		total_theory_classes+=mbc_dic.theory_classes
		total_practice_classes+=mbc_dic.practice_classes

	total_classes=total_theory_classes+total_practice_classes

	#------------

	Dics={
		"page":"1",
		"total":str(len(show_gtp_list)//10+1),
		"records":str(len(show_gtp_list)),
		"rows":myrows,
		"userdata":{"theory_classes":"总节数:","practice_classes":str(total_classes)+"节"}
		}

	with open("static/json/make_gtp.json","w") as f:
		json.dump(Dics,f)

	#----------------------------------------------------
	return render(request,'setrule/m_gtp.html',{
			'all_grade':all_grade,
			'all_profess':all_profess,
			'all_depart':all_depart,
			'select_depart':select_depart,
			'select_profess':select_profess,
			'select_grade':select_grade,
			'edit_public':edit_public,
			'edit_profess':edit_profess
			})

#--------------------------------------------------------------------
@Check_Login
def ins_rule(request):
	return render(request,'setrule/ins_rule.html')

#--------------------------------------------------------------------
@Check_Login
def test_rule(request):
	#------------one1
	sp_maxid=Schoolplace.objects.latest('id').id
	mc_maxid=Myclass.objects.latest('id').id
	if mc_maxid<=sp_maxid:
		maxid=1
	else:
		maxid=0
	#------------one2
	sp_pnum=max(Schoolplace.objects.values('max_seats')).values()[0]
	mc_pnum=max(Myclass.objects.values('myclass_num')).values()[0]
	if sp_pnum>mc_pnum:
		maxnum=1
	else:
		maxnum=0
	#------------one3
	teach_num=models.Maketeachsm.objects.latest('id').id
	mc_maxid=mc_maxid*2
	if teach_num>mc_maxid:
		tnum=1
	else:
		tnum=0
	#------------one4
	mgtp_list = models.Makegradetp.objects.values('depart','grade','profess').distinct()
	gtplay=1
	for mgtp in mgtp_list:
		getlist=models.Makegradetp.objects.filter(
			depart=mgtp['depart'],
			grade=mgtp['grade'],
			profess=mgtp['profess']
			)
		jt_num=0
		for gl in getlist:
			jt_num=jt_num+int(gl.theory_classes)+int(gl.practice_classes)
		if jt_num>30 or jt_num<26:
			gtplay=0
			break
	if mgtp_list.exists()==False:
		gtplay=0
	#------------	
	return render(request,'setrule/test_rules.html',{
		'maxid':maxid,
		'maxnum':maxnum,
		'tnum':tnum,
		'gtplay':gtplay
		})

#--------------------------------------------------------------------
@Check_Login
def eva_report(request):
	from random import choice 	
	ran= choice(weeknum)
	return render(request,'setrule/eva_report.html',{'ran':ran})

#--------------------------------------------------------------------
@Check_Login
def update(request):
	if request.method == 'POST':
		sn=int(request.POST.get('note4',''))
		pl=request.POST.get('note3','')
		tn=request.POST.get('note5','')
		pf=request.POST.get('note6','')		
		myid=request.POST.get('id','')
		models.Makebaseclass.objects.filter(id=myid).update(
			baseclass_stunum=sn,
			schoolplace_class=pl,
			mteacher_name=tn,
			msubject=pf,
			)

	return render(request,'setrule/sindex.html')

#--------------------------------------------------------------------
weeknum=[11,12,13,21,22,23,31,32,33,41,42,43,51,52,53]

weekclasses ={
	11:'星期一第12节',12:'星期一第34节',13:'星期一第56节',
	21:'星期二第12节',22:'星期二第34节',23:'星期二第56节',
	31:'星期三第12节',32:'星期三第34节',33:'星期三第56节',
	41:'星期四第12节',42:'星期四第34节',43:'星期四第56节',
	51:'星期五第12节',52:'星期五第34节',53:'星期五第56节',
}
