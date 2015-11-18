# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20151106_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='votes',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
