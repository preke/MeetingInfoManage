# -*- coding: utf-8 -*-
from MeetingInfoManage.wsgi import *
from User.models import *


def main():
    for i in range(0, 50):
        client, not_exist = Client.objects.get_or_create(name = 'Preke_Boyce_{}'.format(str(i)))
        if not_exist:
            client.sex = 'male'
            client.job = 'doctor_{}'.format(str(i))
            client.office = 'hospital_{}'.format(str(i))
            client.major = 'doctor_{}'.format(str(i))
            client.save()

if __name__ == '__main__':
    main()
    print 'Done!'
