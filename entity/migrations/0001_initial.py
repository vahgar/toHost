# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('source_data', '0005_choosecategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='business_entity',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('profile', models.CharField(null=True, blank=True, max_length=4096)),
                ('services', models.CharField(null=True, blank=True, max_length=4096)),
                ('timings', models.CharField(null=True, blank=True, max_length=150)),
                ('contact_person', models.CharField(null=True, blank=True, max_length=150)),
                ('address', models.CharField(null=True, blank=True, max_length=1000)),
                ('mobile', models.CharField(null=True, blank=True, max_length=10)),
                ('whatsapp', models.CharField(null=True, blank=True, max_length=10)),
                ('Email', models.EmailField(null=True, blank=True, max_length=70)),
                ('website', models.CharField(null=True, blank=True, max_length=70)),
                ('social_media', models.CharField(null=True, blank=True, max_length=300)),
                ('customer_rating', models.FloatField(null=True, blank=True)),
                ('area', models.ForeignKey(to='source_data.Area', null=True, blank=True)),
                ('category', models.ForeignKey(to='source_data.Category', null=True, blank=True)),
                ('city', models.ForeignKey(to='source_data.City', null=True, blank=True)),
                ('locality', models.ForeignKey(to='source_data.Street', null=True, blank=True)),
                ('subcategory', models.ForeignKey(to='source_data.SubCategory', null=True, blank=True)),
            ],
        ),
    ]
