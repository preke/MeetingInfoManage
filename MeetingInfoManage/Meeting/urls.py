# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^leadin$', 'Meeting.views.lead_in', name = 'meeting_lead_in'),
    url(r'^index$', 'Meeting.views.index', name='meeting_index'),
]
