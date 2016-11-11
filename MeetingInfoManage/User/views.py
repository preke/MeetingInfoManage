# -*- coding:utf-8 -*-
from django.shortcuts import render
from User.models import Client
from django.http import HttpResponse
import hashlib
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from Meeting.models import Meeting
from User.models import Client, RSM, RMM
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import *
from MeetingInfoManage.settings import *
from datetime import datetime
import csv
import os
# Create your views here.

def index(request):
        request.session['current'] = 'index'
        client_list = Client.objects.all().order_by('name')
    # try:
        paginator = Paginator(client_list, 15)
        try:
            page = request.GET.get('page', 1)
            page_client_list = paginator.page(page)
        except PageNotAnInteger:
            page_client_list = paginator.page(1)
        except EmptyPage:
            page_client_list = paginator.page(paginator.num_pages)
        info = {'paginator': paginator, 'page_client_list':page_client_list}
        return render(request, 'User/index.html', info)
    # except:
        # return HttpResponse('error')


@csrf_exempt
def lead_in(request):
    if request.method == 'GET':
        return render(request, 'User/client_lead_in.html')
    else :
        client = Client.objects.create()
        client.name = request.POST['name']
        client.sex = request.POST['gender']
        client.birth = request.POST['birth']
        client.job = request.POST['job']
        client.office = request.POST['office']
        client.major = request.POST['major']
        client.title = request.POST['title']
        client.unit = request.POST['unit']
        client.institute_job = request.POST['institute_job']
        client.phone = request.POST['phone']
        client.email = request.POST['email']
        client.region_manager = request.POST['region_manager']
        client.strong_point = request.POST['string_point']
        client.potential_weight = request.POST['potential_weight']
        client.speecher_times = request.POST['speecher_times']
        client.chairman_times = request.POST['chairman_times']
        client.save()
        return HttpResponseRedirect(reverse('client_lead_out'))

@csrf_exempt
def lead_in_extends(request):
    if request.method == 'GET':
        return render(request, 'User/meeting_lead_in_extends.html')
    else :
        # try:
        file = request.FILES['client_lead_in_extends']
        reader = csv.reader(file)
        reader.next() # cut down he head
        record = reader.next()
        while True:
            client, not_exist = Client.objects.get_or_create(name = record[0], sex = record[1],\
                                birth = record[2], job = record[3],office = record[4], major = record[5],\
                                title = record[6], unit = record[7], institute_job = record[8],\
                                phone = record[9], email = record[10], region_manager = record[11], \
                                strong_point = record[12],potential_weight = int(record[13]), \
                                chairman_times = int(record[14]), speecher_times = int(record[15]))
            if (not_exist) :
                client.save()
            try:
                record = reader.next()
            except:
                break
        return HttpResponseRedirect(reverse('index'))
        # except:
            # return HttpResponse('error')




def unicode_2_utf_8(cell):
    if isinstance(cell, unicode):
        return cell.encode('utf-8')
    else :
        return cell

def lead_out(request):
    client_list = Client.objects.all();
    relative_path = 'static/storage/' + 'client';
    csvfile = open(os.path.join(BASE_DIR, relative_path), 'w')
    writer = csv.writer(csvfile)
    writer.writerow(['姓名', '性别', '出生年月', '职务', '科室', '专业', '职称', '单位', '手机',
                    '邮箱', '学会任职', '特长', '负责大区经理', '客户潜力权重', '主席统计', '讲师统计'])
    for client in client_list:
        record = [client.name, client.sex, client.birth, client.job, client.office,\
                  client.major, client.title, client.unit, client.phone]
        record.append(client.email)
        record.append(client.institute_job)
        record.append(client.strong_point)
        record.append(client.region_manager)
        record.append(client.potential_weight)
        record.append(client.chairman_times)
        record.append(client.speecher_times)
        record = [unicode_2_utf_8(cell) for cell in record]
        writer.writerow(record)
    return HttpResponseRedirect(reverse('index'))

@csrf_exempt
def login(request):
    try:
        user_name = request.POST['user_name']
        password = request.POST['password']
        p = hashlib.md5()
        p.update(password)
        password = p.hexdigest()
        rsm = RSM.objects.filter(user_name = user_name, password = password)
        rmm = RMM.objects.filter(user_name = user_name, password = password)

        if rsm.count() > 0 :
            request.session['user_name'] = user_name
            request.session['RSM'] = 'RSM'
        if rmm.count() > 0 :
            request.session['user_name'] = user_name
            request.session['RMM'] = 'RMM'
        return HttpResponseRedirect(reverse(request.session['current']))
    except:
        return HttpResponse("error")

def logout(request):
    del request.session['user_name']
    if request.session.get('RSM', False) :
         del request.session['RSM']
    if request.session.get('RMM', False) :
         del request.session['RMM']
    return HttpResponseRedirect(reverse(request.session['current']))
