# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2023-03-21 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Пол')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Пол',
                'verbose_name_plural': 'Пол',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='worker',
            name='male_or_female',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employees.Gender', verbose_name='Пол'),
        ),
    ]
