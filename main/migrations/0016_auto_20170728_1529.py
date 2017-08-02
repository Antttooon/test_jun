# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 15:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20170728_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='bid_type',
            field=models.CharField(choices=[('cpc', 'CPC'), ('cpm', 'CPM'), ('cpi', 'CPI'), ('cpa', 'CPA'), ('cpv', 'CPV')], default='cpc', max_length=3, verbose_name='bid type'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='channel',
            field=models.ForeignKey(default=main.models.Channel, on_delete=django.db.models.deletion.CASCADE, related_name='channel_channel_name', to='main.Channel', verbose_name='Channel'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='bid_types',
            field=models.CharField(choices=[('cpc', 'CPC'), ('cpm', 'CPM'), ('cpi', 'CPI'), ('cpa', 'CPA'), ('cpv', 'CPV')], default='cpc', max_length=3),
        ),
    ]
