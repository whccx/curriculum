# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-31 19:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reorder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjectall',
            name='five',
        ),
        migrations.RemoveField(
            model_name='subjectall',
            name='four',
        ),
        migrations.RemoveField(
            model_name='subjectall',
            name='six',
        ),
    ]
