# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20151106_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='downvotes',
            field=models.ManyToManyField(related_name='down_votes', to='main.UserProfile'),
        ),
        migrations.AddField(
            model_name='state',
            name='downvotes_count',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='state',
            name='upvotes',
            field=models.ManyToManyField(related_name='up_votes', to='main.UserProfile'),
        ),
        migrations.AddField(
            model_name='state',
            name='upvotes_count',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='state',
            name='votes',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
