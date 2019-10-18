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
            name='orderGoods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('pay', models.DecimalField(max_digits=6, decimal_places=2)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('order_code', models.CharField(primary_key=True, max_length=20, serialize=False)),
                ('total_pay', models.DecimalField(max_digits=7, decimal_places=2)),
                ('order_time', models.DateTimeField(auto_now=True)),
                ('user_address', models.CharField(max_length=40)),
                ('user_name', models.ForeignKey(to='shop_user.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='belong_order',
            field=models.ForeignKey(to='shop_orders.OrderInfo'),
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='goods_name',
            field=models.ForeignKey(to='shop_goods.GoodsInfo'),
        ),
    ]
