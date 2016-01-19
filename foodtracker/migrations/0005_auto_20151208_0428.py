# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodtracker', '0004_auto_20151208_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='foods',
            field=models.ManyToManyField(related_name='restaurants', null=True, to='foodtracker.Food', blank=True),
        ),
    ]
