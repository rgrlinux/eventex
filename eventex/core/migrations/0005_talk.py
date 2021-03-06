# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 00:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170902_0126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('start', models.TimeField(verbose_name='Ínicio')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('speakers', models.ManyToManyField(to='core.Speaker')),
            ],
        ),
    ]
