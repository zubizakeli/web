# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-14 15:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_likediscussion_markdiscussion'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussionresponse',
            name='discussion',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='app1.Discussion'),
        ),
    ]