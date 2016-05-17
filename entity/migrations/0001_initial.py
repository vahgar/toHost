# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('source_data', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='business_entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('profile', models.CharField(blank=True, max_length=4096, null=True)),
                ('services', models.CharField(blank=True, max_length=4096, null=True)),
                ('timings', models.CharField(blank=True, max_length=150, null=True)),
                ('contact_person', models.CharField(blank=True, max_length=150, null=True)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=10, null=True)),
                ('Email', models.EmailField(blank=True, max_length=70, null=True)),
                ('website', models.CharField(blank=True, max_length=70, null=True)),
                ('social_media', models.CharField(blank=True, max_length=300, null=True)),
                ('customer_rating', models.FloatField(blank=True, null=True)),
                ('image_1', models.ImageField(blank=True, upload_to='entity_pics/')),
                ('image_2', models.ImageField(blank=True, upload_to='entity_pics/')),
                ('image_3', models.ImageField(blank=True, upload_to='entity_pics/')),
                ('area', models.ForeignKey(blank=True, null=True, to='source_data.Area')),
                ('category', models.ForeignKey(blank=True, null=True, to='source_data.Category')),
                ('city', models.ForeignKey(blank=True, null=True, to='source_data.City')),
                ('locality', models.ForeignKey(blank=True, null=True, to='source_data.Street')),
                ('subcategory', models.ForeignKey(blank=True, null=True, to='source_data.SubCategory')),
                ('subsubcategory', models.ForeignKey(blank=True, null=True, to='source_data.SubsubCategory')),
            ],
        ),
    ]
