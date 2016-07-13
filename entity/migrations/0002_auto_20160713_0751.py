# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business_entity',
            name='social_media',
            field=models.CharField(max_length=300, default='#', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='business_entity',
            name='website',
            field=models.CharField(max_length=70, default='#', null=True, blank=True),
        ),
    ]
