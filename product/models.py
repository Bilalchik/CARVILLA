from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Brand(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return self.title


class CarBody(models.Model):
    parent = models.ForeignKey('self', on_delete=models.PROTECT, related_name='children', blank=True, null=True)
    title = models.CharField(verbose_name="Название категории", max_length=255)

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])


class Image(models.Model):
    image = models.ImageField(upload_to='media/car_photo')


class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    preview = models.ImageField(upload_to='media/preview_photo')
    images = models.ManyToManyField(Image)
    brands = models.ManyToManyField(Brand)
    car_model = models.CharField(max_length=123)
    slug = models.SlugField()
    year_of_release = models.DateField()
    engine_volume = models.FloatField()
    engine_type = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Бензин'),
            (2, 'Дизель'),
            (3, 'Бензин / Газ'),
            (4, 'Гибрид'),
            (5, 'Электро'),
            (6, 'Газ'),
        )
    )
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    condition = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Хорошее'),
            (2, 'Идеальное'),
            (3, 'Аварийное / не ходу'),
            (4, 'Новое'),
        )
    )
    mileage = models.PositiveIntegerField()
    gearbox = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Автомат'),
            (2, 'Механика'),
            (3, 'Вариатор'),
            (4, 'Робот'),
        )
    )
    rudder_position = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Левый'),
            (2, 'Правый'),
        )
    )
    wheel_drive = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Передний'),
            (2, 'Полный'),
            (3, 'Задний'),
        )
    )
    car_body = models.ForeignKey(CarBody, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00
    )
    status = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Активный'),
            (2, 'Не активен'),
            (3, 'В бане'),
        ),
        default=1
    )
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} | {self.car_model}"


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.PositiveSmallIntegerField(
        choices=(
            (1, 'В обработке'),
            (2, 'Выполнен'),
            (3, 'Отклонен'),
        ),
        default=1
    )

    def __str__(self):
        return f"{self.user} --> {self.car}"

