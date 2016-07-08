# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 22:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import func_sig_registry.registry.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BytesSignature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bytes4_signature', models.CharField(max_length=4, unique=True, validators=[django.core.validators.MinLengthValidator(4)])),
            ],
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('text_signature', models.TextField(unique=True, validators=[func_sig_registry.registry.validators.validate_text_signature, django.core.validators.MinLengthValidator(3)])),
                ('bytes_signature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registry.BytesSignature')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='signature',
            unique_together=set([('text_signature', 'bytes_signature')]),
        ),
    ]
