# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ciljesled', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='start',
            field=models.DateField(default=datetime.date(2014, 12, 25)),
            preserve_default=True,
        ),
    ]
