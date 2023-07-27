# Generated by Django 4.2.3 on 2023-07-27 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "icon",
                    models.ImageField(
                        blank=True, null=True, upload_to="category_icons"
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="frontend.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Delivery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Доставка")),
                ("price", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Images",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="images", verbose_name="Изображение товара"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=100, verbose_name="Название товара"),
                ),
                (
                    "description",
                    models.CharField(max_length=200, verbose_name="Описание товара"),
                ),
                ("price", models.FloatField(verbose_name="Цена товара")),
                ("count", models.IntegerField(verbose_name="Количество товара")),
                (
                    "freeDelivery",
                    models.BooleanField(verbose_name="Бесплатная доставка"),
                ),
                (
                    "available",
                    models.BooleanField(default=True, verbose_name="Доступный"),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("rating", models.IntegerField(default=0)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="frontend.category",
                    ),
                ),
                (
                    "image",
                    models.ManyToManyField(
                        to="frontend.images", verbose_name="Изображение товара"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tags",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Reviews",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author", models.CharField(default="", max_length=255)),
                ("email", models.CharField(default="", max_length=255)),
                ("rating", models.IntegerField(default=0)),
                ("name", models.CharField(default="", max_length=255)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        default="1",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="frontend.products",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(upload_to="avatarts", verbose_name="Аватарка"),
                ),
                ("phone", models.IntegerField()),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="products",
            name="tags",
            field=models.ManyToManyField(to="frontend.tags"),
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("full_name", models.CharField(default="", max_length=100)),
                ("email", models.EmailField(default="", max_length=254)),
                ("phone", models.CharField(default="", max_length=20)),
                ("delivery_type", models.CharField(default="free", max_length=20)),
                ("payment_type", models.CharField(default="online", max_length=20)),
                (
                    "total_cost",
                    models.DecimalField(decimal_places=2, default=0, max_digits=8),
                ),
                ("status", models.CharField(default="accepted", max_length=20)),
                ("city", models.CharField(default="Moscow", max_length=50)),
                ("address", models.CharField(default="red square 1", max_length=100)),
                (
                    "products",
                    models.ManyToManyField(default=None, to="frontend.products"),
                ),
            ],
        ),
    ]
