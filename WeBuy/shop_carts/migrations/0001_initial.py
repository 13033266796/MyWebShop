# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_goods', '0001_initial'),
        ('shop_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('productsNumber', models.IntegerField()),
                ('goods_name', models.ForeignKey(to='shop_goods.GoodsInfo')),
                ('user_name', models.ForeignKey(to='shop_user.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='CollectInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('goods_name', models.ForeignKey(to='shop_goods.GoodsInfo')),
                ('user_name', models.ForeignKey(to='shop_user.UserInfo')),
            ],
        ),
    ]
