# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodtracker', '0003_auto_20151208_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='foods',
            field=models.ManyToManyField(related_name='restaurants', null=True, to='foodtracker.Food'),
        ),
    ]
