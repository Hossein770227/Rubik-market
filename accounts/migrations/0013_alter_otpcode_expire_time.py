# Generated by Django 5.1.5 on 2025-05-14 04:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_otpcode_expire_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpcode',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 5, 14, 4, 52, 46, 141724, tzinfo=datetime.timezone.utc)),
        ),
    ]
