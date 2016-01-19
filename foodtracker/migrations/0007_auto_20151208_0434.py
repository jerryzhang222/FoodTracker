# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodtracker', '0006_auto_20151208_0430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='foods',
        ),
        migrations.AddField(
            model_name='food',
            name='restaurant',
            field=models.ManyToManyField(to='foodtracker.Restaurant', blank=True),
        ),
    ]
