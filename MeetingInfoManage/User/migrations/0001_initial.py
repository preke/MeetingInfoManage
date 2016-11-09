# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('sex', models.CharField(max_length=10, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab')),
                ('birth', models.CharField(max_length=50, verbose_name=b'\xe5\x87\xba\xe7\x94\x9f\xe5\xb9\xb4\xe6\x9c\x88')),
                ('job', models.CharField(max_length=50, verbose_name=b'\xe8\x81\x8c\xe5\x8a\xa1')),
                ('office', models.CharField(max_length=50, verbose_name=b'\xe7\xa7\x91\xe5\xae\xa4')),
                ('major', models.CharField(max_length=50, verbose_name=b'\xe4\xb8\x93\xe4\xb8\x9a')),
                ('title', models.CharField(max_length=50, verbose_name=b'\xe8\x81\x8c\xe7\xa7\xb0')),
                ('unit', models.CharField(max_length=50, verbose_name=b'\xe5\x8d\x95\xe4\xbd\x8d')),
                ('phone', models.CharField(max_length=20, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba')),
                ('email', models.EmailField(max_length=50, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1')),
                ('institute_job', models.CharField(max_length=50, verbose_name=b'\xe5\xad\xa6\xe4\xbc\x9a\xe4\xbb\xbb\xe8\x81\x8c')),
                ('strong_point', models.CharField(max_length=250, verbose_name=b'\xe7\x89\xb9\xe9\x95\xbf')),
                ('region_manager', models.CharField(max_length=50, verbose_name=b'\xe8\xb4\x9f\xe8\xb4\xa3\xe5\xa4\xa7\xe5\x8c\xba\xe7\xbb\x8f\xe7\x90\x86')),
                ('potential_weight', models.IntegerField(default=0, verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7\xe6\xbd\x9c\xe5\x8a\x9b\xe6\x9d\x83\xe9\x87\x8d')),
                ('chairman_times', models.IntegerField(default=0, verbose_name=b'\xe4\xb8\xbb\xe5\xb8\xad\xe7\xbb\x9f\xe8\xae\xa1')),
                ('speecher_times', models.IntegerField(default=0, verbose_name=b'\xe8\xae\xb2\xe5\xb8\x88\xe7\xbb\x9f\xe8\xae\xa1')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
        migrations.CreateModel(
            name='RMM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=250, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('password', models.CharField(max_length=250, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
            ],
            options={
                'verbose_name': '\u5730\u533a\u7ecf\u7406',
                'verbose_name_plural': '\u5730\u533a\u7ecf\u7406',
            },
        ),
        migrations.CreateModel(
            name='RSM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('district', models.CharField(max_length=250, verbose_name=b'\xe5\x9c\xb0\xe5\x8c\xba')),
                ('members', models.ManyToManyField(to='User.Client', verbose_name=b'\xe8\xb4\x9f\xe8\xb4\xa3\xe7\x9a\x84\xe5\xae\xa2\xe6\x88\xb7\xe7\xbe\xa4')),
            ],
            options={
                'verbose_name': '\u5927\u533a\u7ecf\u7406',
                'verbose_name_plural': '\u5927\u533a\u7ecf\u7406',
            },
        ),
    ]
