# Generated by Django 3.0 on 2019-12-22 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarketPlaceApp', '0003_remove_product_img_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img_url',
            field=models.ImageField(default='default.jpg', upload_to='media/'),
            preserve_default=False,
        ),
    ]