# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('source_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locality',
            name='area',
            field=smart_selects.db_fields.ChainedForeignKey(to='source_data.Area', chained_field='city', auto_choose=True, chained_model_field='city'),
        ),
    ]
