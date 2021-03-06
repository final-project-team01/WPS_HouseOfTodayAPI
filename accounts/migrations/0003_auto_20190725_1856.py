# Generated by Django 2.2.3 on 2019-07-25 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190724_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='social_profile',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True, verbose_name='이메일'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='user_image/profile/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='user',
            name='unique_user_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
