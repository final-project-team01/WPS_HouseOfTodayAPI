# Generated by Django 2.2.3 on 2019-08-05 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0012_cronlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cronlog',
            name='cronjob_comment',
            field=models.CharField(default='커뮤니티홈-오늘의 스토리 랜덤 숫자 동작 기록', max_length=300),
        ),
    ]
