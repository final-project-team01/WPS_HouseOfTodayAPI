# Generated by Django 2.2.3 on 2019-08-05 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0013_auto_20190805_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='housewarming',
            name='budget',
            field=models.CharField(default='-', max_length=100),
        ),
    ]
