# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20170728_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='old',
            field=models.IntegerField(default=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='campaign',
            name='bid_type',
            field=models.CharField(choices=[('cpc', 'CPC'), ('cpa', 'CPA'), ('cpi', 'CPI'), ('cpv', 'CPV'), ('cpm', 'CPM')], max_length=3, verbose_name='bid type'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='bid_types',
            field=models.CharField(choices=[('cpc', 'CPC'), ('cpa', 'CPA'), ('cpi', 'CPI'), ('cpv', 'CPV'), ('cpm', 'CPM')], default='cpc', max_length=3),
        ),
    ]
