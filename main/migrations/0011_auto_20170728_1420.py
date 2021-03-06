# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20170728_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='bid_type',
            field=models.CharField(choices=[('cpa', 'CPA'), ('cpv', 'CPV'), ('cpm', 'CPM'), ('cpc', 'CPC'), ('cpi', 'CPI')], max_length=3, verbose_name='bid type'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='bid_types',
            field=models.CharField(choices=[('cpa', 'CPA'), ('cpv', 'CPV'), ('cpm', 'CPM'), ('cpc', 'CPC'), ('cpi', 'CPI')], default='cpc', max_length=3),
        ),
    ]
