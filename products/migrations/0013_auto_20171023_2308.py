# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-23 20:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20171023_2302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='image_folder',
            new_name='image',
        ),
    ]
