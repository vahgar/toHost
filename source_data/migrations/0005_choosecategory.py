# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('source_data', '0004_auto_20160406_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChooseCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('xyz', models.CharField(max_length=255)),
                ('category', models.ForeignKey(to='source_data.Category')),
                ('subCategory', smart_selects.db_fields.ChainedForeignKey(chained_field='category', to='source_data.SubCategory', chained_model_field='category')),
            ],
        ),
    ]
