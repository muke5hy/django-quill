# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import quilljs.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('editor', quilljs.fields.RichTextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
