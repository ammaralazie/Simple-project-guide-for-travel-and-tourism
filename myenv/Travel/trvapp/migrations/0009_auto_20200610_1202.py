# Generated by Django 3.0.5 on 2020-06-10 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trvapp', '0008_contry_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contry',
            name='img10',
        ),
        migrations.RemoveField(
            model_name='contry',
            name='img8',
        ),
        migrations.RemoveField(
            model_name='contry',
            name='img9',
        ),
    ]