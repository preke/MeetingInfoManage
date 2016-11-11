#-*- coding:utf-8 -*-
from django.shortcuts import render
from User.models import Client
from django.http import HttpResponse
import hashlib
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from Meeting.models import Meeting
from User.models import Client
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import *

# Create your views here.
def index(requset):
    return HttpResponse('Under Construction.....')


# @csrf_exempt
def lead_in(request):
    if request.method == 'GET' :
        return render(request, 'Meeting/meeting_lead_in.html')
    else :
        #try:
            meeting = Meeting.objects.create()
            meeting.year = request.POST['date']
            meeting.theme = request.POST['theme']
            meeting.name_of_speecher = request.POST['name_of_speecher']
            meeting.type_of_meeting = request.POST['type_of_meeting']
            meeting.city_of_speecher = request.POST['city_of_speecher']
            meeting.number_of_participant = request.POST['number_of_participant']
            meeting.weight_of_meeting = request.POST['weight_of_meeting']
            meeting.save()
            # return HttpResponseRedirect(reverse('index'))

            return HttpResponseRedirect(reverse('Meeting/index'))
        # except:
        #     return HttpResponse('error')
