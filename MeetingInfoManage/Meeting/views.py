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
from MeetingInfoManage.settings import *
import csv
import os

# Create your views here.
def index(requset):
    return HttpResponse('Under Construction.....')


def meeting_info(request):
    request.session['current'] = 'meeting_info'
    # client_list = Client.objects.all()
    meeting_list = Meeting.objects.all().order_by('-date');
    try:
        paginator = Paginator(meeting_list, 15)
        try:
            page = request.GET.get('page', 1)
            page_meeting_list = paginator.page(page)
        except PageNotAnInteger:
            page_meeting_list = paginator.page(1)
        except EmptyPage:
            page_meeting_list = paginator.page(paginator.num_pages)
        info = {'paginator': paginator, 'page_meeting_list':page_meeting_list}
        return render(request, 'Meeting/meeting_info.html', info)
    except:
        return HttpResponse('error')

@csrf_exempt
def lead_in(request):
    if request.method == 'GET' :
        return render(request, 'Meeting/meeting_lead_in.html')
    else :
        try:
            meeting = Meeting.objects.create()
            meeting.year = request.POST['date']
            meeting.theme = request.POST['theme']
            meeting.name_of_speecher = request.POST['name_of_speecher']
            meeting.type_of_speecher = request.POST['type_of_speecher']
            meeting.city_of_speecher = request.POST['city_of_speecher']
            meeting.number_of_participant = request.POST['number_of_participant']
            meeting.type_of_meeting = request.POST['type_of_meeting']
            meeting.weight_of_meeting = request.POST['weight_of_meeting']
            meeting.save()
            return HttpResponseRedirect(reverse('meeting_lead_out'))
        except:
            return HttpResponse('error');

@csrf_exempt
def lead_in_extends(request):
    if request.method == 'GET':
        return render(request, 'Meeting/meeting_lead_in_extends.html')
    else :
        file = request.FILES['meeting_lead_in_extends']
        reader = csv.reader(file)
        reader.next() # cut down he head
        record = reader.next()
        while True :
            meeting, not_exist = Meeting.objects.get_or_create(date = record[0], number = record[1], theme = record[2],\
                                                            name_of_speecher = record[3], type_of_speecher = record[4],\
                                                            city_of_speecher = record[5], number_of_participant = record[6],\
                                                            type_of_meeting = record[7], weight_of_meeting = record[8])
            if not_exist :
                meeting.save()
            try:
                record = reader.next()
            except:
                break
        return HttpResponseRedirect(reverse("index"))











def unicode_2_utf_8(cell):
    if isinstance(cell, unicode):
        return cell.encode('utf-8')
    else :
        return cell

def lead_out(request):
    meeting_list = Meeting.objects.all();
    relative_path = 'static/storage/meeting'
    csvfile = open(os.path.join(BASE_DIR, relative_path), 'w')
    writer = csv.writer(csvfile)
    writer.writerow(['年月', '编号', '活动主题', '讲者名字', '讲者类型', '讲者城市', '参会人数', '会议类型', '会议权重'])
    for meeting in meeting_list:
        record = [meeting.date, meeting.number, meeting.theme, meeting.name_of_speecher,
                  meeting.type_of_speecher,meeting.city_of_speecher, meeting.number_of_participant,
                  meeting.type_of_meeting, meeting.weight_of_meeting];
        record = [unicode_2_utf_8(cell) for cell in record]
        writer.writerow(record)
    return HttpResponseRedirect(reverse('index'))
