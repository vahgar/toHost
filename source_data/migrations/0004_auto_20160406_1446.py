# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('source_data', '0003_auto_20160404_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('category', models.ForeignKey(to='source_data.Category')),
            ],
        ),
        migrations.AlterField(
            model_name='locality',
            name='area',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='city', to='source_data.Area', chained_model_field='city'),
        ),
    ]
