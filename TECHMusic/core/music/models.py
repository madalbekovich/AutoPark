from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name="Название")
    preview_img = models.ImageField(upload_to='songs/category/img', )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Song(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория', null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name="Название песни")
    file = models.FileField(upload_to='songs/', verbose_name="Аудиофайл")
    img = models.ImageField(verbose_name='Обложка песни', null=True, blank=True)
    time_of_music = models.TimeField(verbose_name="Время музыки")
    count_listener = models.IntegerField(verbose_name="Кл-во слушателей")
    text = models.TextField(verbose_name='Текст песни')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"