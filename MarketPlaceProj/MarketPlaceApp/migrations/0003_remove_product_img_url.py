# Generated by Django 3.0 on 2019-12-19 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MarketPlaceApp', '0002_auto_20191218_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='img_url',
        ),
    ]
