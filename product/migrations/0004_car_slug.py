# Generated by Django 5.0.3 on 2024-04-11 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_car_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
