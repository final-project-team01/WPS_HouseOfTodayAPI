# Generated by Django 2.2.3 on 2019-07-30 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_auto_20190730_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='photocomment',
            name='author_profile_image',
            field=models.TextField(blank=True),
        ),
    ]
