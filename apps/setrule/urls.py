# -*- coding: utf-8 -*-
from __future__ import unicode_literals
app_name = 'setrule'
from django.conf.urls import url

from setrule import views as setrule_views
#from setrule import change

urlpatterns = [
    url(r'^$', setrule_views.sindex,name='sindex'),
    url(r'^sindex.html$', setrule_views.sindex,name='sindex'),
    
    url(r'^update$', setrule_views.update , name = 'update'),
    url(r'^m_tsm.html$', setrule_views.m_tsm , name ='tsm_edit'),
    url(r'^m_gtp.html$', setrule_views.m_gtp , name ='gtp_edit'),
    
    url(r'^sindex.html$', setrule_views.sindex , name='make_bmt'),
    url(r'^m_tsm.html$', setrule_views.m_tsm , name='make_tsm'),
    url(r'^m_gtp.html$', setrule_views.m_gtp , name='make_gtp'),    
    url(r'^ins_rule.html$', setrule_views.ins_rule , name='ins_rules'),
    url(r'^test_rules.html$', setrule_views.test_rule , name='test_rules'),

    url(r'^eva_report.html$', setrule_views.eva_report , name='eva_report'),
]
