# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-08 13:15
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("app", "0007_statemodel_connect")]

    operations = [
        migrations.CreateModel(
            name="ConnectModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("json", django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            options={"verbose_name": "Connect", "verbose_name_plural": "Connects"},
        )
    ]
