# Generated by Django 3.0 on 2019-12-22 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MarketPlaceApp', '0004_product_img_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated_at',
        ),
    ]
