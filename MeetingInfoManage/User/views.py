from django.shortcuts import render
from User.models import Client
from django.http import HttpResponse
import hashlib
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from Meeting.models import Meeting
from User.models import Client, RSM, RMM
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def lead_in(request):
    if request.method == 'GET':
        return render(request, 'User/client_lead_in.html')
    else :
        client = Client.objects.create()
        client.name = request.POST['name']
        client.sex = request.POST['sex']
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
        client.weight_of_meeting = request.POST['weight_of_meeting']
        client.speecher_times = request.POST['speecher_times']
        client.chairman_times = request.POST['chairman_times']
        client.save()
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
