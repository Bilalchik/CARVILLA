# Generated by Django 5.0.3 on 2024-04-09 20:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123)),
            ],
        ),
        migrations.CreateModel(
            name='CarBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название категории')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='product.carbody')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=123)),
                ('year_of_release', models.DateField()),
                ('engine_volume', models.FloatField()),
                ('engine_type', models.PositiveSmallIntegerField(choices=[(1, 'Бензин'), (2, 'Дизель'), (3, 'Бензин / Газ'), (4, 'Гибрид'), (5, 'Электро'), (6, 'Газ')])),
                ('condition', models.PositiveSmallIntegerField(choices=[(1, 'Хорошее'), (2, 'Идеальное'), (3, 'Аварийное / не ходу'), (4, 'Новое')])),
                ('mileage', models.PositiveIntegerField()),
                ('gearbox', models.PositiveSmallIntegerField(choices=[(1, 'Автомат'), (2, 'Механика'), (3, 'Вариатор'), (4, 'Робот')])),
                ('rudder_position', models.PositiveSmallIntegerField(choices=[(1, 'Левый'), (2, 'Правый')])),
                ('wheel_drive', models.PositiveSmallIntegerField(choices=[(1, 'Передний'), (2, 'Полный'), (3, 'Задний')])),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Активный'), (2, 'Не активен'), (3, 'В бане')], default=1)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('brands', models.ManyToManyField(to='product.brand')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('car_body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.carbody')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.color')),
            ],
        ),
    ]
