# Generated by Django 4.0.3 on 2022-05-02 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_image_alter_product_price_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True, verbose_name='URL'),
        ),
    ]
