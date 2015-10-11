# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Smasher',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('name_first', models.CharField(max_length=50)),
                ('name_last', models.CharField(max_length=50)),
                ('gamer_tag', models.CharField(blank=True, max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'smashers',
                'verbose_name': 'smasher',
            },
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('status', models.CharField(verbose_name='Status', max_length=100, choices=[('IN', 'Interested'), ('AP', 'Approved'), ('CO', 'Confirmed')])),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('start_time', models.TimeField(default=django.utils.timezone.now, verbose_name='Time')),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('capacity', models.IntegerField(default=0, verbose_name='Capacity')),
                ('num_confirmed', models.IntegerField(default=0, verbose_name='Number Confirmed')),
                ('location', models.CharField(max_length=200)),
                ('notes', models.TextField(verbose_name='Notes', blank=True, max_length=200)),
                ('host', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='attendee',
            name='event',
            field=models.ForeignKey(to='web.Event'),
        ),
        migrations.AddField(
            model_name='attendee',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='smasher',
            name='events',
            field=models.ManyToManyField(to='web.Event', through='web.Attendee'),
        ),
        migrations.AddField(
            model_name='smasher',
            name='friends',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='friends_rel_+'),
        ),
    ]
