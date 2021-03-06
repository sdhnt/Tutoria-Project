# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 11:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20171028_0248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sessions',
            old_name='booked_time',
            new_name='bookedTime',
        ),
        migrations.RenameField(
            model_name='sessions',
            old_name='student_id',
            new_name='studentID',
        ),
        migrations.RenameField(
            model_name='sessions',
            old_name='tutor_id',
            new_name='tutorID',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_first_name',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='is_tutor',
            new_name='isTutor',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_last_name',
            new_name='lastName',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_booking_status',
        ),
    ]
