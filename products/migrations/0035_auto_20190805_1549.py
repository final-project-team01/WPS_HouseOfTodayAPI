# Generated by Django 2.2.3 on 2019-08-05 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0034_cronlog_cronjob_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='cronlog',
            name='cronjob_comment',
            field=models.CharField(default='스토어홈-오늘의 딜 랜덤 숫자 동작 기록', max_length=300),
        ),
    ]
