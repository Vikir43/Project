# Generated by Django 4.2.7 on 2023-11-25 14:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myshop", "0002_product_count_product_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(default="product-images/default.jpg", upload_to=""),
        ),
    ]