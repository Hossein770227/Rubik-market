# Generated by Django 5.1.5 on 2025-05-14 05:14

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='category Name')),
            ],
            options={
                'verbose_name': 'categories',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('brand', models.CharField(max_length=150, verbose_name='brand')),
                ('text', ckeditor.fields.RichTextField(verbose_name='text')),
                ('price_without_discount', models.PositiveIntegerField(verbose_name='price without discount')),
                ('price_with_discount', models.PositiveIntegerField(verbose_name='price with discount')),
                ('image', models.ImageField(blank=True, null=True, upload_to='cover/', verbose_name='image')),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='active ?')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Release Date')),
                ('rating', models.CharField(blank=True, choices=[(5, '⭐⭐⭐⭐⭐'), (4, '⭐⭐⭐⭐'), (3, '⭐⭐⭐'), (2, '⭐⭐'), (1, '⭐')], max_length=10, verbose_name='rating')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ['title'],
                'indexes': [models.Index(fields=['title', 'brand'], name='products_pr_title_d5b4d5_idx')],
            },
        ),
    ]
