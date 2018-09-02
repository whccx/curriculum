from __future__ import unicode_literals

from django.conf.urls import url
from mydata.views import Show,Show_myclass
from mydata import models
app_name = 'mydata'


urlpatterns = [
    url(r'^1$', Show.as_view(),name='mydata_dp'),
    url(r'^2$', Show.as_view(model=models.Professional),name='mydata_pf'),
    url(r'^3$', Show.as_view(model=models.Schoolplace),name='mydata_sp'),
    url(r'^4$', Show.as_view(model=models.Grade),name='mydata_grade'),
    url(r'^5$', Show.as_view(model=models.Public_subjects),name='mydata_ps'),
    url(r'^6$', Show.as_view(model=models.Profess_subjects),name='mydata_ms'),
    url(r'^7$', Show.as_view(model=models.Parttimeteacher),name='mydata_ptt'),
    url(r'^8$', Show.as_view(model=models.Fulltimeteacher),name='mydata_ftt'),
    url(r'^9$', Show.as_view(model=models.Substituteteacher),name='mydata_stt'),

    url(r'^myclass.html$', Show_myclass.as_view(),name='mydata_myclass'),
    url(r'^myclass.html$', Show_myclass.as_view(),name='restart'),
]