# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodtracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='ndbno',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='food',
            name='calories',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='foods',
            field=models.ManyToManyField(related_name='restaurants', to='foodtracker.Food', blank=True),
        ),
    ]
