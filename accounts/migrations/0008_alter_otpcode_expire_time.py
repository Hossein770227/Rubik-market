# Generated by Django 5.1.5 on 2025-05-10 07:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_otpcode_expire_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpcode',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 5, 10, 7, 32, 0, 476084, tzinfo=datetime.timezone.utc)),
        ),
    ]
