# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='birth',
            field=models.CharField(default=b'birth', max_length=50, verbose_name=b'\xe5\x87\xba\xe7\x94\x9f\xe5\xb9\xb4\xe6\x9c\x88'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(default=b'email', max_length=50, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1'),
        ),
        migrations.AlterField(
            model_name='client',
            name='institute_job',
            field=models.CharField(default=b'institute', max_length=50, verbose_name=b'\xe5\xad\xa6\xe4\xbc\x9a\xe4\xbb\xbb\xe8\x81\x8c'),
        ),
        migrations.AlterField(
            model_name='client',
            name='job',
            field=models.CharField(default=b'job', max_length=50, verbose_name=b'\xe8\x81\x8c\xe5\x8a\xa1'),
        ),
        migrations.AlterField(
            model_name='client',
            name='major',
            field=models.CharField(default=b'major', max_length=50, verbose_name=b'\xe4\xb8\x93\xe4\xb8\x9a'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(default=b'\xe5\x90\x8d\xe5\xad\x97', max_length=50, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='client',
            name='office',
            field=models.CharField(default=b'office', max_length=50, verbose_name=b'\xe7\xa7\x91\xe5\xae\xa4'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(default=b'phone', max_length=20, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba'),
        ),
        migrations.AlterField(
            model_name='client',
            name='region_manager',
            field=models.CharField(default=b'manage', max_length=50, verbose_name=b'\xe8\xb4\x9f\xe8\xb4\xa3\xe5\xa4\xa7\xe5\x8c\xba\xe7\xbb\x8f\xe7\x90\x86'),
        ),
        migrations.AlterField(
            model_name='client',
            name='sex',
            field=models.CharField(default=b'\xe6\x80\xa7\xe5\x88\xab', max_length=10, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab'),
        ),
        migrations.AlterField(
            model_name='client',
            name='strong_point',
            field=models.CharField(default=b'string_point', max_length=250, verbose_name=b'\xe7\x89\xb9\xe9\x95\xbf'),
        ),
        migrations.AlterField(
            model_name='client',
            name='title',
            field=models.CharField(default=b'title', max_length=50, verbose_name=b'\xe8\x81\x8c\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='client',
            name='unit',
            field=models.CharField(default=b'unit', max_length=50, verbose_name=b'\xe5\x8d\x95\xe4\xbd\x8d'),
        ),
        migrations.AlterField(
            model_name='rmm',
            name='password',
            field=models.CharField(default=b'password', max_length=250, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81'),
        ),
        migrations.AlterField(
            model_name='rmm',
            name='user_name',
            field=models.CharField(default=b'user_name', max_length=250, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='rsm',
            name='district',
            field=models.CharField(default=b'district', max_length=250, verbose_name=b'\xe5\x9c\xb0\xe5\x8c\xba'),
        ),
        migrations.AlterField(
            model_name='rsm',
            name='members',
            field=models.ManyToManyField(default=b'member', to='User.Client', verbose_name=b'\xe8\xb4\x9f\xe8\xb4\xa3\xe7\x9a\x84\xe5\xae\xa2\xe6\x88\xb7\xe7\xbe\xa4'),
        ),
        migrations.AlterField(
            model_name='rsm',
            name='name',
            field=models.CharField(default=b'name', max_length=250, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97'),
        ),
    ]
