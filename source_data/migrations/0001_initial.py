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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ChooseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('category', models.ForeignKey(to='source_data.Category')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('area', smart_selects.db_fields.ChainedForeignKey(chained_model_field='city', chained_field='city', to='source_data.Area')),
                ('city', models.ForeignKey(to='source_data.City', related_name='cityofloc')),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('area', models.ForeignKey(to='source_data.Area')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('category', models.ForeignKey(to='source_data.Category')),
            ],
        ),
        migrations.CreateModel(
            name='SubsubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('subCategory', models.ForeignKey(to='source_data.SubCategory')),
            ],
        ),
        migrations.AddField(
            model_name='locality',
            name='street',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='area', chained_field='area', to='source_data.Street'),
        ),
        migrations.AddField(
            model_name='choosecategory',
            name='subCategory',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='category', chained_field='category', to='source_data.SubCategory'),
        ),
        migrations.AddField(
            model_name='choosecategory',
            name='subsubCategory',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='subCategory', chained_field='subCategory', blank=True, to='source_data.SubsubCategory', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='city',
            field=models.ForeignKey(to='source_data.City'),
        ),
    ]
