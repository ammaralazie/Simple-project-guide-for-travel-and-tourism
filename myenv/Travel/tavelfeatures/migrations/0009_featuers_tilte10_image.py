# Generated by Django 3.0.5 on 2020-06-15 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tavelfeatures', '0008_auto_20200615_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuers',
            name='tilte10_image',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]