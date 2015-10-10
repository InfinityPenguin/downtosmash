# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Smasher',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('name_first', models.CharField(max_length=50)),
                ('name_last', models.CharField(max_length=50)),
                ('gamer_tag', models.CharField(max_length=50, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(verbose_name='Time')),
                ('start_date', models.DateField(verbose_name='Date')),
                ('capacity', models.IntegerField(verbose_name='Capacity', default=0)),
                ('location', models.CharField(max_length=200)),
                ('notes', models.TextField(verbose_name='Notes', max_length=200, blank=True)),
                ('host', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='smasher',
            name='events',
            field=models.ManyToManyField(to='web.Event'),
        ),
        migrations.AddField(
            model_name='smasher',
            name='friends',
            field=models.ManyToManyField(related_name='friends_rel_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
