# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Smasher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name_first', models.CharField(max_length=50)),
                ('name_last', models.CharField(max_length=50)),
                ('gamer_tag', models.CharField(max_length=50, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'smasher',
                'verbose_name_plural': 'smashers',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('start_time', models.TimeField(verbose_name='Time', default=django.utils.timezone.now)),
                ('start_date', models.DateField(verbose_name='Date', default=django.utils.timezone.now)),
                ('capacity', models.IntegerField(verbose_name='Capacity', default=0)),
                ('location', models.CharField(max_length=200)),
                ('notes', models.TextField(verbose_name='Notes', blank=True, max_length=200)),
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
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='friends_rel_+'),
        ),
    ]
