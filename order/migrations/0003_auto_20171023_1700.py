# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-23 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20171023_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_price',
            new_name='order_price',
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='total_price',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]