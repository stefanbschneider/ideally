# Generated by Django 3.0.7 on 2020-07-27 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200727_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(default='#FF0000', max_length=7),
        ),
    ]