# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
url(r'^login$', 'User.views.login', name = 'login'),
url(r'^logout$', 'User.views.logout', name = 'logout'),
    url(r'^leadin$', 'User.views.lead_in', name = 'client_lead_in'),
    url(r'^leadin_extends$', 'User.views.lead_in_extends', name = 'client_lead_in_extends'),
    url(r'^leadout$', 'User.views.lead_out', name = 'client_lead_out'),
]
