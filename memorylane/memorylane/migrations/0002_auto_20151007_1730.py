# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('memorylane', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memory',
            name='author',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memory',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2015, 10, 7, 22, 27, 52, 296000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memory',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memory',
            name='image',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memory',
            name='name',
            field=models.CharField(default='Memory Name', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(default='Example Bio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2015, 10, 7, 22, 29, 7, 75000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='email@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.CharField(default='', max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='memories',
            field=models.CharField(default='', max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='password', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='propic',
            field=models.CharField(default='propic.jpg', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='testusername', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='memory',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]
