# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-22 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0002_create_apply_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='fundtype',
            name='workflow',
            field=models.CharField(choices=[('single', 'Single Stage'), ('double', 'Two Stage')], default='single', max_length=100),
        ),
    ]
