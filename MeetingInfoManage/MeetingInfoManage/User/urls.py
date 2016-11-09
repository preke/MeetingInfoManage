# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^leadin$', 'User.views.lead_in', name = 'client_lead_in'),
    url(r'^login$', 'User.views.login', name = 'login'),
    url(r'^logout$', 'User.views.logout', name = 'logout'),
]
