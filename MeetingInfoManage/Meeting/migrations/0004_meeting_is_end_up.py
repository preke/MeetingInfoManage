# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting', '0003_auto_20161109_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='is_end_up',
            field=models.BooleanField(default=False, verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f'),
        ),
    ]
