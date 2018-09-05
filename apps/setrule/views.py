# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from setrule import models
from mydata import models as mm
from django.db.models import Max,Sum
import json

from users.views import Check_Login
#--------------------------------------------------------------------
@Check_Login
def sindex(request):		
	sl = models.Makebaseclass.objects.all()
	if sl.exists()==False:create_mbc()
	Dics = []
	for md in sl:
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
	sp=mm.Schoolplace.objects.all()
	mylist=stradd(sp,'schoolplace_num')
	#------------------
	ep = mm.Profess_subjects.objects.all()
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
		if i==len(ep):mstr=mstr+e+str(":")+e
		else:mstr=mstr+e+str(":")+e+str(";")
		i+=1
	return mstr

def create_mbc():
	ss = mm.Myclass.objects.all()	
	for sl in ss:
		pflist=mm.Professional.objects.get(pf_name=sl.m_pf_name)
		glist=mm.Grade.objects.get(grade_name=sl.m_grade_name,g_pf_name=sl.m_pf_name)
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
	a=models.Maketeachsm.objects
	tp = mm.Parttimeteacher.objects.all()
	for t in tp:
		n=a.filter(teacher_name=t.pt_name)
		if n.exists()==False:
			i=a.all()
			if i.exists()==False:i=1
			else:i=int(a.latest('id').id)+1
			a.create(teacher_name=t.pt_name,id=i,teacher_type='兼职')
	#---------
	tb = mm.Fulltimeteacher.objects.all()
	for t in tb:
		n=a.filter(teacher_name=t.ft_name)
		if n.exists()==False:
			i=int(a.latest('id').id)+1
			a.create(teacher_name=t.ft_name,id=i,teacher_type='全职')
	#---------
	ts = mm.Substituteteacher.objects.all()
	for s in ts:
		n=a.filter(teacher_name=s.st_name)
		if n.exists()==False:
			i=int(a.latest('id').id)+1
			a.create(teacher_name=s.st_name,id=i,teacher_type='代课')
	#-------------------------------------
	#teach subject and time
	pb={}
	sp = mm.Public_subjects.objects.all()
	for d in sp:pb[d.id] = d.ps_name

	pf={}
	ss = mm.Profess_subjects.objects.all()
	for d in ss:pf[d.id] = d.ms_name

	if request.method == 'POST':
		b=request.POST
		my_teacher_name=b.get('my_teacher_name','')
		maxme = b.get('spinner1','')
		minme = b.get('spinner2','')
		c_profess = b.get('profess','')
		c_public = b.get('public','')
		c_mtime = b.get('mtime','')
		c_untime = b.get('untime','')
		c_radio = b.get('form-field-radio','')
		cd = b.getlist('duallistbox1')
		ml = ""
		for i in range(len(cd)):			
			if i==0:ml = str(cd[i])
			else:ml = ml + ',' + str(cd[i])
		if c_radio=="1":c_profess = ml
		if c_radio=="2":c_public = ml
		if c_radio=="3":c_mtime = ml
		if c_radio=="4":c_untime = ml
		a.filter(id=my_teacher_name).update(
			profess_subject=c_profess,
			public_subject=c_public,
			max_classes=maxme,
			min_classes=minme,
			must_time=c_mtime,
			unable_time=c_untime,
			)
		
	smls = a.all()
	Dics = []
	for m in smls:
		dic_ccx = {
		"id": m.id,
		"teacher_name": m.teacher_name,
		"teacher_type": m.teacher_type,
		"public_subject" : m.public_subject,
		"profess_subject" : m.profess_subject,
		"max_classes" : m.max_classes,
		"min_classes" : m.min_classes,
		"must_time" : m.must_time,
		"unable_time" : m.unable_time
		}		
		Dics.append(dic_ccx)

	return render(
			request,'setrule/m_tsm.html',
			{
			'Subject_public_dics':json.dumps(pb),
			'Subject_profess_dics':json.dumps(pf),
			'Dics':json.dumps(Dics),				
			'weekclasses':json.dumps(weekclasses),
			},
			)

#--------------------------------------------------------------------	
@Check_Login
def m_gtp(request):
	a=models.Makegradetp.objects
	select_depart="";select_profess="";select_grade=""
	sml = models.Makebaseclass.objects.all()
	all_grade=[];all_profess=[];all_depart=[]
	for m in sml:
		aa=m.basegrade_name
		bb=m.baseprofess_name
		cc=m.basedepart_name
		if aa not in all_grade:	all_grade.append(aa)		
		if bb not in all_profess:all_profess.append(bb)
		if cc not in all_depart:all_depart.append(cc)		
	if select_grade=="":select_grade=all_grade[0]
	if select_profess=="":select_profess=all_profess[0]
	if select_depart=="":select_depart=all_depart[0]
	#----------------------------
	pb=[];pf=[]
	pbs = mm.Public_subjects.objects.all()
	pfs = mm.Profess_subjects.objects.all()
	for e in pbs:pb.append(e.ps_name)	
	for e in pfs:pf.append(e.ms_name)
	#----------------------------
	if request.method == 'POST':
		b=request.POST
		myid=b.get('id','0')
		ms=b.get('subject_name','')
		mt=int(b.get('theory_classes','0'))
		mpc=int(b.get('practice_classes','0'))
		mpo=int(b.get('prior_order','0'))
		my_cha=b.get('oper','')
		if my_cha=="edit":
			est=b.get('subject_type','')
			a.filter(id=myid).update(
				subject_name=ms,
				theory_classes=mt,
				practice_classes=mpc,
				prior_order=mpo,
				subject_type=est,
				)
		if my_cha=="del":a.filter(id=myid).delete()
		if my_cha=="add":
			add_grade=b.get('grade','')
			add_profess=b.get('profess','')
			add_depart=b.get('depart','')
			ast=b.get('subject_type','')
			sml = a.all()
			meid=0
			for m in sml:
				if m.id>meid:
					lsid=m.id
					if lsid-meid>1:
						break						
					else:meid=m.id
			a.create(
				id=meid+1,
				subject_name=ms,
				theory_classes=mt,
				practice_classes=mpc,
				prior_order=mpo,
				grade=add_grade,
				profess=add_profess,
				depart=add_depart,
				subject_type=ast,
				)
		if my_cha=="my_search":
			select_depart=b.get('select1','0')
			select_profess=b.get('select2','0')
			select_grade=b.get('select3','0')
			
	#------------------------------------------
	sl =a.filter(depart=select_depart,profess=select_profess,grade=select_grade)	
	myrows=[];e=[];co=[];Dics={};tt=0;tp=0;ta=0
	#-----------
	for d in sl:
		co=[
			d.id,
			d.subject_type,
			d.subject_name,			
			d.theory_classes,			
			d.practice_classes,
			d.prior_order,			
			d.grade,
			d.profess,
			d.depart
		]
		e={"id":str(d.id),"cell":co}
		myrows.append(e)
		tt+=d.theory_classes
		tp+=d.practice_classes
	ta=tt+tp

	#------------

	Dics={
		"page":"1",
		"total":str(len(sl)//10+1),
		"records":str(len(sl)),
		"rows":myrows,
		"userdata":{"theory_classes":"总节数:","practice_classes":str(ta)+"节"}
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
			'edit_public':pb,
			'edit_profess':pf,
			})

#--------------------------------------------------------------------
@Check_Login
def ins_rule(request):
	return render(request,'setrule/ins_rule.html')

#--------------------------------------------------------------------
@Check_Login
def test_rule(request):
	#------------one1
	sp_maxid=mm.Schoolplace.objects.latest('id').id
	mc_maxid=mm.Myclass.objects.latest('id').id
	if mc_maxid<=sp_maxid:maxid=1
	else:maxid=0
	#------------one2
	sp_pnum=mm.Schoolplace.objects.aggregate(a=Max('max_seats')).get('a')
	mc_pnum=mm.Myclass.objects.aggregate(a=Max('myclass_num')).get('a')
	if sp_pnum>mc_pnum:maxnum=1
	else:maxnum=0
	#------------one3\
	teach_num=models.Maketeachsm.objects.latest('id').id
	mc_maxid=mc_maxid*2
	if teach_num>mc_maxid:tnum=1
	else:tnum=0
	#------------one4
	a=models.Makegradetp.objects
	mgtp_list = a.values('depart','grade','profess').distinct()
	gtplay=1
	for mgtp in mgtp_list:
		getlist=a.filter(
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
	if mgtp_list.exists()==False:gtplay=0
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
	a=models.Makebaseclass.objects.all()
	b=models.Makegradetp.objects
	t=0;tt=0;ttt=0;ty=0;music=0
	for c in a:
		e=b.filter(depart=c.basedepart_name,grade=c.basegrade_name,profess=c.baseprofess_name)
		for f in e:
			t+=f.theory_classes
			if f.subject_name=='体育':
				ty+=f.theory_classes
			if f.subject_name=='音乐':
				music+=f.theory_classes
			if f.profess!='电子电工':
				tt+=f.practice_classes
			else:
				if f.subject_name=='计算机基础':
					tt+=f.practice_classes
				else:
					ttt+=f.practice_classes
	to=t+tt+ttt
	return render(request,'setrule/eva_report.html',{'t':t,'ty':ty,'music':music,'tt':tt,'ttt':ttt,'to':to})

#--------------------------------------------------------------------
@Check_Login
def update(request):
	if request.method == 'POST':
		a=request.POST
		sn=int(a.get('note4',''))
		pl=a.get('note3','')
		tn=a.get('note5','')
		pf=a.get('note6','')		
		myid=a.get('id','')
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

a=1
