# Generated by Django 2.1.5 on 2019-02-09 02:39

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190209_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='related',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='blog.BlogPage'),
        ),
    ]