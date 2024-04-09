# Generated by Django 5.0.3 on 2024-04-09 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/car_photo')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='preview',
            field=models.ImageField(default=1, upload_to='media/preview_photo'),
            preserve_default=False,
        ),
    ]
