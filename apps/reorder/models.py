# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Subjectall(models.Model):
	classnum = models.IntegerField(default=0)
	week = models.IntegerField(default=0)
	one = models.IntegerField(default=0)
	two = models.IntegerField(default=0)
	three = models.IntegerField(default=0)
		