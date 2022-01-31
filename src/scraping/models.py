import jsonfield
from django.db import models

# Create your models here.
from django.utils.text import slugify

def default_url():
    return {"work": "", "dou": ""}

class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название населенного пункта', unique=True )
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class  Meta:
        verbose_name = 'Название населенного пункта'
        verbose_name_plural = 'Название населенных пунктов'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.name), allow_unicode=True)
        super().save(*args, **kwargs)

class Language(models.Model): #TODO: Переименовать в тип имущества
    name = models.CharField(max_length=50, verbose_name='Язык программирования', unique=True )
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class  Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.name), allow_unicode=False)
        super().save(*args, **kwargs)

class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Заголовок вакансии')
    company = models.CharField(max_length=250, verbose_name='Компания')
    description = models.TextField(verbose_name='Описание')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
    language = models.ForeignKey('language', on_delete=models.CASCADE, verbose_name='Язык программирования')
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title


class Error(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    data = jsonfield.JSONField()


class Url(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
    language = models.ForeignKey('language', on_delete=models.CASCADE, verbose_name='Язык программирования')
    url_data = jsonfield.JSONField(default=default_url)
    
    class Meta:
        unique_together = ('city', 'language')