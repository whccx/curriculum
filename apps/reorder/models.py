# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Subjectall(models.Model):
	classnum = models.IntegerField(default=0)
	week = models.IntegerField(default=0)
	one = models.CharField(max_length=30,blank='true')
	two = models.CharField(max_length=30,blank='true')
	three = models.CharField(max_length=30,blank='true')
		