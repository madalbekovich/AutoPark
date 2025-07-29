from django.db import models

class Authors(models.Model):
    """Автор песни"""
    first_name = models.CharField(verbose_name="Имя")
    last_name = models.CharField(verbose_name="Фамилия")
    email = models.EmailField(verbose_name="E-mail", unique=True)
    phone = models.CharField(verbose_name="Номер телефона", unique=True)

    short_bio_text = models.TextField(verbose_name="Краткая био")
    avatar = models.ImageField(verbose_name='Аватар автора', upload_to='authors/avatar')
    music_of_count = models.IntegerField(verbose_name='Кл-во музыки', null=True, blank=True)

    class Meta:
        verbose_name = 'Авторы песни'
        verbose_name_plural = 'Авторы песни'
        ordering = ['id']
        unique_together = ('id', )