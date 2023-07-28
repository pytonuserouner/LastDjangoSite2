# Generated by Django 4.2.3 on 2023-07-28 07:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("frontend", "0003_alter_products_images_alter_products_title_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="images",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="media/images/",
                verbose_name="Изображение товара",
            ),
        ),
    ]