from django.db import models
from datetime import datetime


class Category(models.Model):
    name = models.CharField('Категория', max_length=160, unique=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Source(models.Model):
    name = models.CharField('Источник', max_length=160, unique=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Источник'
        verbose_name_plural = 'Источники'


class Vacancies(models.Model):
    title = models.CharField('Название вакансии', max_length=160)
    url = models.URLField('Ссылка на объявление', max_length=160, unique=True)
    text = models.TextField('Описание вакансии', null=True)
    published = models.DateTimeField('Дата публикации', default=datetime.now())
    category = models.ForeignKey\
        (Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    source = models.ForeignKey\
        (Source, verbose_name='Источник', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    objects = models.Manager()
