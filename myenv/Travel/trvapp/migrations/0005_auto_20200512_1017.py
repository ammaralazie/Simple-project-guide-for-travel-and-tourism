# Generated by Django 3.0.5 on 2020-05-12 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trvapp', '0004_auto_20200511_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='contry',
            name='culture',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contry',
            name='langunge',
            field=models.TextField(blank=True, null=True),
        ),
    ]
