# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-20 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0069_auto_20171120_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='wallet',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]