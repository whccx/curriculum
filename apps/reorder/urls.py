# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from reorder import views
app_name = 'reorder'

urlpatterns = [    
	url(r'^start.html$', views.start,name='start'),
]
