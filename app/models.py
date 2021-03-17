from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Note(models.Model):
    """заметка"""
    name = models.CharField('Название заметки', max_length=45, default='Без названия')
    completed = models.BooleanField('Выполненно', default=False, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['completed', 'date']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('note_products', kwargs={'pk': self.pk})


class Value(models.Model):
    """величина измерения"""
    name = models.CharField('Величина измерения', max_length=256)

    class Meta:
        verbose_name = 'Величина измерения'
        verbose_name_plural = 'Величины измерения'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """товар"""
    note = models.ForeignKey(Note, verbose_name='Заметка', related_name='products', on_delete=models.CASCADE)
    name = models.CharField('Название продукта', max_length=256)
    value = models.ForeignKey(Value, verbose_name='Величина измерения', on_delete=models.CASCADE)
    count = models.DecimalField('Количество', max_digits=10, decimal_places=1)
    completed = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
