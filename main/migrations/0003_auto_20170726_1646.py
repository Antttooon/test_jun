# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170726_1631'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='channel',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='campaign',
            name='bid_type',
            field=models.CharField(choices=[('cpi', 'CPI'), ('cpv', 'CPV'), ('cpa', 'CPA'), ('cpm', 'CPM'), ('cpc', 'CPC')], default='cpc', max_length=3, verbose_name='bid type'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='bid_types',
            field=models.CharField(choices=[('cpi', 'CPI'), ('cpv', 'CPV'), ('cpa', 'CPA'), ('cpm', 'CPM'), ('cpc', 'CPC')], default='cpc', max_length=3),
        ),
    ]
