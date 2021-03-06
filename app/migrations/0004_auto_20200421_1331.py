# Generated by Django 3.0.5 on 2020-04-21 13:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200421_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timecard',
            name='timeIn',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='timecard',
            name='timeOut',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='verificationcode',
            name='expiryDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 21, 13, 36, 24, 189337, tzinfo=utc)),
        ),
    ]
