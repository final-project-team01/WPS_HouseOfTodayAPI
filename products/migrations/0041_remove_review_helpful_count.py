# Generated by Django 2.2.3 on 2019-08-16 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0040_auto_20190816_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='helpful_count',
        ),
    ]