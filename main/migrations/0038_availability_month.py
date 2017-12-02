# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20171031_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='month',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Jan'), (1, 'Feb'), (2, 'Mar'), (3, 'Apr'), (4, 'May'), (5, 'Jun'), (6, 'Jul'), (7, 'Aug'), (8, 'Sep'), (9, 'Oct'), (10, 'Nov'), (11, 'Dec')], default=10),
            preserve_default=False,
        ),
    ]