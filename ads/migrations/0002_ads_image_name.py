# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads_image',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
