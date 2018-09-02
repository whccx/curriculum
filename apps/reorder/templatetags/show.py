# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from reorder import models
from django import template

register = template.Library()

@register.filter
def get_list(d,m):
	if hasattr(d, m):
		return d.get(m)