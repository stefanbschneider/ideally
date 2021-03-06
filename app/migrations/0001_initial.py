# Generated by Django 3.0.7 on 2020-07-22 06:03

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=5000)),
                ('creation_date', models.DateTimeField(auto_now=True, verbose_name='date created')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('tags', models.ManyToManyField(to='app.Tag')),
            ],
        ),
    ]
