# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-04 17:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offside', '0003_auto_20171204_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('hour', models.TimeField()),
                ('stadium', models.CharField(max_length=50)),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchaway', to='offside.Team')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchhome', to='offside.Team')),
            ],
        ),
    ]
