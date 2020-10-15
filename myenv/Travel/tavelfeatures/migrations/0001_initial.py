# Generated by Django 3.0.5 on 2020-05-12 19:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Featuers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tilte', models.CharField(max_length=500)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('contant1', models.TextField(blank=True, null=True)),
                ('contant2', models.TextField(blank=True, null=True)),
                ('contant3', models.TextField(blank=True, null=True)),
                ('contant5', models.TextField(blank=True, null=True)),
                ('contant6', models.TextField(blank=True, null=True)),
                ('create', models.DateTimeField(default=datetime.datetime.now)),
                ('img1', models.ImageField(upload_to='pictuer2')),
                ('img2', models.ImageField(upload_to='pictuer2')),
                ('img3', models.ImageField(upload_to='pictuer2')),
                ('img4', models.ImageField(upload_to='pictuer2')),
                ('img5', models.ImageField(upload_to='pictuer2')),
            ],
        ),
    ]