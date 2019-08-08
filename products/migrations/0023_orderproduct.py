# Generated by Django 2.2.3 on 2019-07-24 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0022_productordercart'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.CharField(max_length=50)),
                ('rec_zipcode', models.CharField(max_length=10)),
                ('rec_address1', models.CharField(max_length=300)),
                ('rec_address2', models.CharField(max_length=200)),
                ('rec_phone_number', models.CharField(max_length=30)),
                ('rec_comment', models.CharField(max_length=500)),
                ('orderer_name', models.CharField(max_length=50)),
                ('orderer_email', models.CharField(max_length=100)),
                ('orderer_phone_number', models.CharField(max_length=30)),
                ('total_product_price', models.PositiveIntegerField(default=0)),
                ('deliver_price', models.PositiveIntegerField(default=0)),
                ('total_payment', models.PositiveIntegerField(default=0)),
                ('product_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='products.ProductOption')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
