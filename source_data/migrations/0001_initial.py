# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('street', models.CharField(max_length=1000)),
                ('area', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='city', chained_model_field='city', to='source_data.City')),
                ('city', models.ForeignKey(related_name='cityofloc', to='source_data.City')),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='city',
            field=models.ForeignKey(to='source_data.City'),
        ),
    ]
