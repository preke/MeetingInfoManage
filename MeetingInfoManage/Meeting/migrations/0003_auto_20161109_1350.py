# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting', '0002_auto_20161105_0823'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meeting',
            options={'verbose_name': '\u4f1a\u8bae', 'verbose_name_plural': '\u4f1a\u8bae'},
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='month',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='year',
        ),
        migrations.AddField(
            model_name='meeting',
            name='date',
            field=models.CharField(default=b'2016/11/11', max_length=100, verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
        ),
    ]
