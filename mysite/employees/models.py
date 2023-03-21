from django.db import models
from django.urls import reverse


class Worker(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    surname = models.CharField(max_length=200, verbose_name='Отчество')
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')
    age = models.DateField()
    male_or_female = models.ForeignKey('Gender', on_delete=models.PROTECT, verbose_name='Пол')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    pos = models.ForeignKey('Position', on_delete=models.PROTECT, verbose_name='Должность')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    def get_absolute_url(self):  # ссылка на данный класс
        return reverse('worker', kwargs={'worker_slug': self.slug})

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'
        ordering = ['last_name']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категории')
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # ссылка на данный класс
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Position(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Должность')
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # ссылка на данный класс
        return reverse('Position', kwargs={'pos_slug': self.slug})

    class Meta:
        verbose_name = 'должность'
        verbose_name_plural = 'должности'
        ordering = ['name']


class Gender(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Пол')
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # ссылка на данный класс
        return reverse('gender', kwargs={'gen_slug': self.slug})

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'
        ordering = ['id']
