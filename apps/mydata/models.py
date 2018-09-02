# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
# =================ccx================ #

class Department(models.Model):
	depart_name = models.CharField(max_length=30)

class Professional(models.Model):
	pf_name = models.CharField(max_length=30) #pf:professional
	dp_name = models.CharField(max_length=30) #dp:depart

class Schoolplace(models.Model):
	building_name = models.CharField(max_length=30,blank='true')
	building_floor = models.CharField(max_length=30,blank='true')
	schoolplace_name = models.CharField(max_length=30)
	schoolplace_num = models.CharField(max_length=10,blank='true')
	max_seats = models.IntegerField()

class Grade(models.Model):
	grade_name = models.CharField(max_length=15)
	year = models.CharField(max_length=10)
	class_num = models.IntegerField() #open class num
	g_pf_name = models.CharField(max_length=30,blank='true') #pf:professional

	def __str__():
		return self.text


class Myclass(models.Model):
	myclass_name = models.CharField(max_length=45)
	m_grade_name = models.CharField(max_length=15)
	m_pf_name = models.CharField(max_length=30)
	myclass_num = models.IntegerField()

class Public_subjects(models.Model):
	ps_name = models.CharField(max_length=30)  #公共科目名字

class Profess_subjects(models.Model):
	ms_name = models.CharField(max_length=30) #专业科目名字
	ms_pf_name = models.CharField(max_length=30) #所属专业

class Parttimeteacher(models.Model):
	pt_name = models.CharField(max_length=30) #pt:parttime_teacher

class Fulltimeteacher(models.Model):
	ft_name = models.CharField(max_length=30) #pt:fulltime_teacher

class Substituteteacher(models.Model):
	st_name = models.CharField(max_length=30) #st:substitute_teacher
