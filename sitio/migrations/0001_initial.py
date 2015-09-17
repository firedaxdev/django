# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, db_index=True)),
                ('slug', models.SlugField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('contenido', django_markdown.models.MarkdownField()),
                ('publicado', models.DateField(db_index=True, auto_now_add=True)),
                ('categoria', models.ForeignKey(to='sitio.Categoria')),
            ],
        ),
    ]
