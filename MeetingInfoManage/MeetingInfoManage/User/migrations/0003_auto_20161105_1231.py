# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20161105_0823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rsm',
            name='name',
        ),
        migrations.AddField(
            model_name='rsm',
            name='user_name',
            field=models.CharField(default=b'user_name', max_length=250, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97'),
        ),
        migrations.AlterField(
            model_name='rmm',
            name='password',
            field=models.CharField(default=b'e10adc3949ba59abbe56e057f20f883e', max_length=250, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81'),
        ),
    ]
