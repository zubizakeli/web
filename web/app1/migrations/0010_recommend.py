# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-12 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_discussion_add_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.IntegerField()),
                ('reader_id', models.IntegerField()),
            ],
        ),
    ]
