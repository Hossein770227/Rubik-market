# Generated by Django 5.1.5 on 2025-05-14 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_with_discount',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='price with discount'),
        ),
    ]
