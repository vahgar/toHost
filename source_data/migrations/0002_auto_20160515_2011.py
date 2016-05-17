# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import smart_selects.db_fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('source_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choosecategory',
            name='subsubCategory',
            field=smart_selects.db_fields.ChainedForeignKey(to='source_data.SubsubCategory', chained_model_field='subCategory', chained_field='subCategory', default=datetime.datetime(2016, 5, 15, 20, 11, 56, 428000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
