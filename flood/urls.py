# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.shortcuts import render
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'flood.views.home', name='home'),
    # url(r'^flood/', include('flood.foo.urls')),


)

urlpatterns += patterns('django.contrib.auth.views',
    (r'^login$', 'login', {'template_name': 'login.html'}, 'login'),
    (r'^logout$', 'logout', {'next_page': '/'}, 'logout'),
)

urlpatterns += patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
