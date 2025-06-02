import random
from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    phone = models.CharField("Номер телефона", unique=True, max_length=999999)

    is_blocked = models.BooleanField(default=False, verbose_name="Заблокирован")
    block_reason = models.TextField(null=True, blank=True, verbose_name="Причина блокировки")

    code = models.IntegerField("Код активации", null=True, blank=True)
    activated = models.BooleanField("Активировано", default=False)

    notification = models.BooleanField("Получать уведомления", default=False)

    USERNAME_FIELD = "phone"
    objects = CustomUserManager()

    def __str__(self):
        return str(self.phone)

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        self.code = int(random.randint(10_00, 99_99))
        super(User, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"