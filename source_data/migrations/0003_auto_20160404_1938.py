# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('source_data', '0002_auto_20160404_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('area', models.ForeignKey(to='source_data.Area')),
            ],
        ),
        migrations.AlterField(
            model_name='locality',
            name='street',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='area', chained_model_field='area', to='source_data.Street'),
        ),
    ]
