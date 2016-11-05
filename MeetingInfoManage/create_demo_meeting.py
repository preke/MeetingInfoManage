from MeetingInfoManage.wsgi import *
from Meeting.models import *

def main():
    for i in range(0, 50):
        meeting, not_exist = Meeting.objects.get_or_create(year = 2017 + i)
        if not_exist:
            meeting.month = 11
            meeting.number = '12345679'+ str(meeting.year)
            meeting.theme ='meeting is a good theme , and it is meeting_{}'.format(str(i))
            meeting.name_of_speecher = 'speecher_{}'.format(str(i))
            meeting.type_of_speecher = 'boss'
            meeting.city_of_speecher = 'universe'
            meeting.weight_of_meeting = i
            meeting.save()

if __name__ == '__main__':
    main()
    print 'Done!'
