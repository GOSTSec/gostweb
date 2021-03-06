# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-21 20:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepositTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('txid', models.CharField(max_length=64, unique=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.Account')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.Address')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WithdrawalTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('txid', models.CharField(max_length=64, unique=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=35)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.Account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='account',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='address',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
