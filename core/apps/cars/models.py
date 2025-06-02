from . import choices
from django.db import models
from apps.users.models import User

class CarType(models.Model):
    name = models.CharField('Тип кузова', max_length=100)
    img = models.ImageField('Фото типа машины', upload_to='car/car_type/', null=True, blank=True)

    def __str__(self):
        return self.name

class DealType(models.Model):
    name = models.CharField('Тип сделки', max_length=100)

    def __str__(self):
        return self.name

class VehicleType(models.Model):
    name = models.CharField('Тип Автомобиля', max_length=100)

    def __str__(self):
        return self.name

class CarMark(models.Model):
    id_car_type = models.ForeignKey('CarType', on_delete=models.CASCADE)
    name = models.CharField('Название марки', max_length=100)
    img = models.ImageField('Фото автомобиля', upload_to='car/mark/', null=True, blank=True)
    is_popular = models.BooleanField(default=False, verbose_name='Популярная марка')

    def __str__(self):
        return self.name

class CarModel(models.Model):
    id_car_mark = models.ForeignKey("CarMark", on_delete=models.CASCADE, related_name="car_mark")
    name = models.CharField("Название модели", max_length=100)
    is_popular = models.BooleanField(default=False, verbose_name='Популярная модель')

    def __str__(self):
        return f"{self.name}"

class CarGeneration(models.Model):
    id_car_model = models.ForeignKey("CarModel", on_delete=models.CASCADE)
    year_begin = models.CharField("Начало выпуска от", null=True, max_length=255)
    year_end = models.CharField("Год выпуска до", null=True, max_length=255)
    seria = models.CharField('Серия', max_length=255)
    img = models.ImageField('Фото поколение', null=True, blank=True, upload_to='car/generation/')

class Transmission(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Fuel(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class GearBox(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class SteeringWheel(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class CarColor(models.Model):
    name = models.CharField("Название", max_length=300, null=True)
    color = models.CharField("Цвет", max_length=300, null=True)
    def __str__(self):
        return self.name

class CarOwner(models.Model):
    name = models.CharField("Владелец", max_length=300, null=True)
    def __str__(self):
        return self.name

class Condition(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Custom(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Availability(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Currency(models.Model):
    name = models.CharField(max_length=50)
    sign = models.CharField(max_length=10)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CarPost(models.Model):
    """Модель для объявление автомобилей"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deal_type = models.ForeignKey('DealType', on_delete=models.CASCADE)

    car_type = models.ForeignKey('CarType', on_delete=models.CASCADE, verbose_name='Тип кузова')
    car_brand = models.ForeignKey('CarMark', on_delete=models.CASCADE, verbose_name='Марка')
    car_model = models.ForeignKey('CarModel', on_delete=models.CASCADE, verbose_name='Модель')
    car_generation = models.ForeignKey('CarGeneration', on_delete=models.CASCADE, verbose_name='Поколение')

    fuel = models.ForeignKey('Fuel', on_delete=models.CASCADE, verbose_name='Тип двигателя')
    transmission = models.ForeignKey('Transmission', on_delete=models.CASCADE, verbose_name='Привод')
    vehicle_type = models.ForeignKey('VehicleType', on_delete=models.CASCADE, verbose_name='Тип автомобиля')
    gearbox = models.ForeignKey('Gearbox', on_delete=models.CASCADE, verbose_name='Коробка передач')
    color = models.ForeignKey('CarColor', on_delete=models.CASCADE, verbose_name='Цвет')
    count_owner = models.ForeignKey('CarOwner', on_delete=models.CASCADE, verbose_name='К-лво Владелец')
    steering_wheel = models.ForeignKey('SteeringWheel', on_delete=models.CASCADE, verbose_name='Руль')
    condition = models.ForeignKey('Condition', on_delete=models.CASCADE, verbose_name='Техническое состояние')
    custom = models.ForeignKey('Custom', on_delete=models.CASCADE, verbose_name='Техническое состояние')
    availability = models.ForeignKey('Availability', on_delete=models.CASCADE, verbose_name='Наличии')
    region = models.ForeignKey('Region', on_delete=models.CASCADE, verbose_name='Регион продажи')

    year = models.IntegerField(default=1900, verbose_name='Год выпуска')
    engine_volume = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Объем двигателя (л)')

    mileage = models.IntegerField(default=000000, verbose_name='Пробег')
    distance_unit = models.CharField(choices=choices.DISTANCE_UNIT_CHOICES, default='KM', verbose_name='Измерения расстояния')
    price = models.DecimalField(max_digits=12, decimal_places=1, default=0.0, verbose_name='Цена')
    currency = models.CharField(default='Сом', choices=choices.CURRENCY, verbose_name='Валюта цены')

    vin_code = models.CharField(default='01KG000ABC', verbose_name='VIN код')
    description = models.TextField(null=True, blank=True, verbose_name='Дополнительная информация')
    ctc_phone_1 = models.CharField(default='+996', max_length=50, verbose_name='Телефонный номер для контакта1')
    ctc_phone_2 = models.CharField(default='+996', max_length=50, verbose_name='Телефонный номер для контакта2')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

class CarImage(models.Model):
    image = models.ForeignKey('CarPost', on_delete=models.CASCADE, verbose_name='Картинки автомобиля')
    img = models.ImageField()

    class Meta:
        verbose_name = 'Картинки автомобиля'
        verbose_name_plural = 'Картинки автомобиля'
