# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-20 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='comment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
