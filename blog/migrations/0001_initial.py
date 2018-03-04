# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.core.fields
import wagtail.core.blocks
import wagtail.images.blocks
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0019_verbose_names_cleanup'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True,
                                                  auto_created=True,
                                                  primary_key=True, serialize=False, to='wagtailcore.Page', on_delete=django.db.models.deletion.CASCADE)),
                ('author', models.CharField(max_length=255)),
                ('date', models.DateField(verbose_name=b'Post date')),
                ('body', wagtail.core.fields.StreamField([(b'heading', wagtail.core.blocks.CharBlock(classname=b'full title')), (b'paragraph', wagtail.core.blocks.RichTextBlock()), (b'image', wagtail.images.blocks.ImageChooserBlock())])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
