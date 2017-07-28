# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170726_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='bid_type',
            field=models.CharField(choices=[('cpm', 'CPM'), ('cpa', 'CPA'), ('cpv', 'CPV'), ('cpi', 'CPI'), ('cpc', 'CPC')], default='cpc', max_length=3, verbose_name='bid type'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='bid_types',
            field=models.CharField(choices=[('cpm', 'CPM'), ('cpa', 'CPA'), ('cpv', 'CPV'), ('cpi', 'CPI'), ('cpc', 'CPC')], default='cpc', max_length=3),
        ),
    ]