"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.conf.urls import url,include
from django.views.generic.base import RedirectView
from . import views as project_views
from users import views as users_views
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$',users_views.logout_view,name='logout'),
    url(r'^login.html$',users_views.login_view,name='login'),

    url(r'^$', project_views.index,name='index'),
    url(r'^index.html$', project_views.index,name='index'),
    url(r'^favicon.ico$',RedirectView.as_view(url=r'static/favicon.ico')),
    url(r'^users/', include('users.urls',namespace='users')),
    
    url(r'^setrule/', include('setrule.urls',namespace='setrule')),
    url(r'^mydata/', include('mydata.urls',namespace='mydata')),
    url(r'^other/', include('other.urls',namespace='other')),
    url(r'^reorder/', include('reorder.urls',namespace='reorder')),
]
