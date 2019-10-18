# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('goods_name', models.CharField(max_length=40)),
                ('goods_image', models.ImageField(upload_to='goodsImage')),
                ('goods_price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('goods_unit', models.CharField(max_length=10)),
                ('goods_valueNumber', models.IntegerField()),
                ('goods_clickNumber', models.IntegerField()),
                ('goods_originPlace', models.CharField(max_length=10)),
                ('goods_introduction', models.CharField(max_length=100)),
                ('goods_content', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('typeName', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='goods_type',
            field=models.ForeignKey(to='shop_goods.GoodsType'),
        ),
    ]
