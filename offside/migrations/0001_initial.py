# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-04 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('point', models.IntegerField()),
                ('manager', models.CharField(max_length=30)),
                ('played_match', models.IntegerField()),
                ('win', models.IntegerField()),
                ('lost', models.IntegerField()),
                ('draw', models.IntegerField()),
                ('average', models.IntegerField()),
                ('League', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offside.League')),
            ],
        ),
    ]