# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('user_name', models.CharField(max_length=20, null=True)),
                ('user_pwd', models.CharField(max_length=40)),
                ('user_number', models.CharField(max_length=11)),
                ('user_nickname', models.CharField(max_length=20, null=True)),
                ('user_mail', models.CharField(max_length=20, null=True)),
                ('user_address', models.CharField(max_length=100, default='省,市,县,详细地址')),
                ('user_telephone', models.IntegerField(max_length=12, null=True)),
                ('user_youbian', models.CharField(max_length=6, null=True)),
                ('user_score', models.CharField(max_length=100, default='0')),
                ('user_money', models.CharField(max_length=100, default='0')),
                ('user_gender', models.BooleanField(default=True)),
            ],
        ),
    ]
