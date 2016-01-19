# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodtracker', '0007_auto_20151208_0434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='foods',
            field=models.ManyToManyField(related_name='restaurants', to='foodtracker.Food', blank=True),
        ),
    ]
