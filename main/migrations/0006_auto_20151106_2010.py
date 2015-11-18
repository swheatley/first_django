# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20151106_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='downvotes',
        ),
        migrations.RemoveField(
            model_name='state',
            name='downvotes_count',
        ),
        migrations.RemoveField(
            model_name='state',
            name='upvotes',
        ),
        migrations.RemoveField(
            model_name='state',
            name='upvotes_count',
        ),
        migrations.RemoveField(
            model_name='state',
            name='votes',
        ),
    ]
