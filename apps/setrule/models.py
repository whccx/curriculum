# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# =================ccx================ #

# make_base_message_table
class Makebaseclass(models.Model):
	baseclass_name = models.CharField(max_length=30)
	basegrade_name = models.CharField(max_length=30)
	baseclass_year = models.CharField(max_length=30)
	baseclass_num = models.IntegerField(default=0)
	baseprofess_name = models.CharField(max_length=30) #专业名字
	basedepart_name = models.CharField(max_length=30)
	schoolplace_class = models.CharField(max_length=30,blank='true')
	baseclass_stunum = models.IntegerField(default=0)
	mteacher_name = models.CharField(max_length=30,blank='true')
	msubject = models.CharField(max_length=30,blank='true')


#make_teach_subject_message
class Maketeachsm(models.Model):
	teacher_name = models.CharField(max_length=30)
	teacher_type = models.CharField(max_length=30)
	profess_subject = models.CharField(max_length=30,blank='true') #专业科目名字
	public_subject = models.CharField(max_length=30,blank='true') #公共科目名字
	max_classes = models.IntegerField(default=30)
	min_classes = models.IntegerField(default=0)
	must_time = models.CharField(max_length=30,blank='true')
	unable_time = models.CharField(max_length=30,blank='true')

#make_grade_teach_play
class Makegradetp(models.Model):
	depart = models.CharField(max_length=30,blank='true')
	grade = models.CharField(max_length=30,blank='true')
	profess = models.CharField(max_length=30,blank='true')
	subject_name = models.CharField(max_length=30)
	subject_type = models.CharField(max_length=30,blank='true')
	theory_classes = models.IntegerField(default=0)
	practice_classes = models.IntegerField(default=0)
	prior_order = models.IntegerField(default=0)
