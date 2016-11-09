# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(default=2016, verbose_name=b'\xe5\xb9\xb4')),
                ('month', models.IntegerField(default=1, verbose_name=b'\xe6\x9c\x88')),
                ('number', models.CharField(max_length=250, null=True, verbose_name=b'\xe7\xbc\x96\xe5\x8f\xb7')),
                ('theme', models.CharField(max_length=250, null=True, verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe4\xb8\xbb\xe9\xa2\x98')),
                ('name_of_speecher', models.CharField(max_length=250, null=True, verbose_name=b'\xe8\xae\xb2\xe5\xb8\x88\xe5\x90\x8d\xe5\xad\x97')),
                ('type_of_speecher', models.CharField(max_length=250, null=True, verbose_name=b'\xe8\xae\xb2\xe8\x80\x85\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('city_of_speecher', models.CharField(max_length=250, null=True, verbose_name=b'\xe8\xae\xb2\xe8\x80\x85\xe5\x9f\x8e\xe5\xb8\x82')),
                ('number_of_participant', models.IntegerField(default=0, verbose_name=b'\xe5\x8f\x82\xe4\xbc\x9a\xe4\xba\xba\xe6\x95\xb0')),
                ('type_of_meeting', models.CharField(max_length=250, null=True, verbose_name=b'\xe4\xbc\x9a\xe8\xae\xae\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('weight_of_meeting', models.IntegerField(default=0, verbose_name=b'\xe4\xbc\x9a\xe8\xae\xae\xe6\x9d\x83\xe9\x87\x8d')),
            ],
            options={
                'ordering': ['-year', '-month'],
                'verbose_name': '\u4f1a\u8bae',
                'verbose_name_plural': '\u4f1a\u8bae',
            },
        ),
    ]
