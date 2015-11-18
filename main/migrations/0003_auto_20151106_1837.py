# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20151106_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='downvotes_count',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='state',
            name='upvotes_count',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
