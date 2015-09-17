# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='contenido',
            field=redactor.fields.RedactorField(verbose_name='Text'),
        ),
    ]
