# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-21 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_auto_20171021_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposittransaction',
            name='amount',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=15),
        ),
        migrations.AddField(
            model_name='withdrawaltransaction',
            name='amount',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=15),
        ),
    ]
