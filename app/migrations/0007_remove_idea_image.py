# Generated by Django 3.0.7 on 2020-09-17 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200727_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='image',
        ),
    ]
