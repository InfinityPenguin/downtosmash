# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Date and time of event')),
                ('capacity', models.IntegerField(verbose_name='Capacity of event', default=0)),
                ('location', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_first', models.CharField(max_length=50)),
                ('name_last', models.CharField(max_length=50)),
                ('gamer_tag', models.CharField(max_length=50, blank=True)),
                ('events', models.ManyToManyField(to='web.Event')),
                ('friends', models.ManyToManyField(related_name='friends_rel_+', to='web.User')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='host',
            field=models.ForeignKey(to='web.User'),
        ),
    ]
