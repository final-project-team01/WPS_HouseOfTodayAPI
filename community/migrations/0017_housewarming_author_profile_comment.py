# Generated by Django 2.2.3 on 2019-08-07 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0016_auto_20190807_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='housewarming',
            name='author_profile_comment',
            field=models.TextField(blank=True),
        ),
    ]