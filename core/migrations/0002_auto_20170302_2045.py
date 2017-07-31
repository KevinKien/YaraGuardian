# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-03-02 20:45
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmeta',
            name='category_options',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=75), default=list, size=None),
        ),
        migrations.AddField(
            model_name='groupmeta',
            name='category_required',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='groupmeta',
            name='source_options',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=75), default=list, size=None),
        ),
        migrations.AddField(
            model_name='groupmeta',
            name='source_required',
            field=models.BooleanField(default=True),
        ),
    ]
