# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statecapital',
            name='state',
            field=models.OneToOneField(null=True, blank=True, to='main.State'),
        ),
    ]
