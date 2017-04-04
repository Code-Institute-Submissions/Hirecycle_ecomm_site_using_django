# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email_address', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=2000)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
