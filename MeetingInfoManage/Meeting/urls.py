# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^leadin$', 'Meeting.views.lead_in', name = 'meeting_lead_in'),
    url(r'leadin_extends', 'Meeting.views.lead_in_extends', name = 'meeting_lead_in_extends'),
    url(r'^leadout$', 'Meeting.views.lead_out', name = 'meeting_lead_out'),
    url(r'^meeting_info$', 'Meeting.views.meeting_info', name='meeting_info'),
]
