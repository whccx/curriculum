# -*- coding: utf-8 -*-

from django.shortcuts import render

from setrule import models

def sindex(request):
	if request == 'POST':
		myid=request.POST('id')
		myplace=request.POST('note2')
	models.Makebaseclass.objects.filter(id=myid).update(schoolplace_class=myplace)
