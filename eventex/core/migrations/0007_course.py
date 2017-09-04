# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20170903_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('start', models.TimeField(blank=True, null=True, verbose_name='Ínicio')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('slots', models.IntegerField(verbose_name='Vagas')),
                ('speakers', models.ManyToManyField(blank=True, to='core.Speaker', verbose_name='palestrantes')),
            ],
            options={
                'verbose_name': 'palestra',
                'abstract': False,
                'verbose_name_plural': 'palestras',
            },
        ),
    ]
