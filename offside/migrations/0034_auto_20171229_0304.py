# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-29 00:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offside', '0033_commentnews_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentnews',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
