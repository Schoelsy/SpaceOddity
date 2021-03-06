# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-15 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20171029_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='house',
            name='house_photo',
            field=models.CharField(default='SOME STRING', max_length=500),
        ),
        migrations.AddField(
            model_name='house',
            name='name',
            field=models.CharField(default='SOME STRING', max_length=50),
        ),
        migrations.AddField(
            model_name='planet',
            name='description',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='planet',
            name='description_long',
            field=models.CharField(default='SOME STRING', max_length=1000),
        ),
        migrations.AddField(
            model_name='planet',
            name='main_photo',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='planet',
            name='small_photo',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]
