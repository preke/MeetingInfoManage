# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='city_of_speecher',
            field=models.CharField(default=b'city', max_length=250, verbose_name=b'\xe8\xae\xb2\xe8\x80\x85\xe5\x9f\x8e\xe5\xb8\x82', blank=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='name_of_speecher',
            field=models.CharField(default=b'speecher', max_length=250, verbose_name=b'\xe8\xae\xb2\xe5\xb8\x88\xe5\x90\x8d\xe5\xad\x97', blank=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='number',
            field=models.CharField(default=b'number', max_length=250, verbose_name=b'\xe7\xbc\x96\xe5\x8f\xb7', blank=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='theme',
            field=models.CharField(default=b'theme', max_length=250, verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe4\xb8\xbb\xe9\xa2\x98', blank=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='type_of_meeting',
            field=models.CharField(default=b'meeting', max_length=250, verbose_name=b'\xe4\xbc\x9a\xe8\xae\xae\xe7\xb1\xbb\xe5\x9e\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='type_of_speecher',
            field=models.CharField(default=b'speecher', max_length=250, verbose_name=b'\xe8\xae\xb2\xe8\x80\x85\xe7\xb1\xbb\xe5\x9e\x8b', blank=True),
        ),
    ]
