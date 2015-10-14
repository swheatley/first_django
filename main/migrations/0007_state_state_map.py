# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20151012_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='state_map',
            field=models.ImageField(null=True, upload_to=b'state_map', blank=True),
        ),
    ]
