# -*- coding: utf-8 -*-
from __future__ import unicode_literals
app_name = 'other'
from django.conf.urls import url

from other import views
#from setrule import change

urlpatterns = [
	url(r'^manual.html$', views.manual,name='manual'),
]
