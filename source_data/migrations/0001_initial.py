# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-15 08:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ChooseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='source_data.Category')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', smart_selects.db_fields.ChainedForeignKey(chained_field='city', chained_model_field='city', on_delete=django.db.models.deletion.CASCADE, to='source_data.Area')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cityofloc', to='source_data.City')),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='source_data.Area')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='source_data.Category')),
            ],
        ),
        migrations.CreateModel(
            name='SubsubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('subCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='source_data.SubCategory')),
            ],
        ),
        migrations.AddField(
            model_name='locality',
            name='street',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='area', chained_model_field='area', on_delete=django.db.models.deletion.CASCADE, to='source_data.Street'),
        ),
        migrations.AddField(
            model_name='choosecategory',
            name='subCategory',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='category', chained_model_field='category', on_delete=django.db.models.deletion.CASCADE, to='source_data.SubCategory'),
        ),
        migrations.AddField(
            model_name='choosecategory',
            name='subsubCategory',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='subCategory', chained_model_field='subCategory', on_delete=django.db.models.deletion.CASCADE, to='source_data.SubsubCategory'),
        ),
        migrations.AddField(
            model_name='area',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='source_data.City'),
        ),
    ]
