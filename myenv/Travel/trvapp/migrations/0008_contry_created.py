# Generated by Django 3.0.5 on 2020-06-10 11:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trvapp', '0007_auto_20200610_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='contry',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
