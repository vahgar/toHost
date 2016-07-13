# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0002_auto_20160713_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business_entity',
            name='social_media',
            field=models.CharField(default='#', max_length=300),
        ),
        migrations.AlterField(
            model_name='business_entity',
            name='website',
            field=models.CharField(default='#', max_length=70),
        ),
    ]
