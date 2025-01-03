# Generated by Django 4.2 on 2024-11-30 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("electronics", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="networkelectronics",
            name="link_type",
            field=models.CharField(
                choices=[
                    ("FC", "Завод"),
                    ("RN", "Розничная сеть"),
                    ("IE", "Индивидуальный предприниматель"),
                ],
                help_text="Выберите тип организации",
                max_length=100,
                verbose_name="Тип организации",
            ),
        ),
    ]
