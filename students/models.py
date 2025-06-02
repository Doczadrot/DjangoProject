"""
Модели приложения - определяем структуру данных 📊

Для новичков:
Это как чертежи для таблиц в базе данных 📐
Каждый класс Model - это отдельная таблица
Каждое поле - колонка в таблице

Пример:
class Student(models.Model):
    name = models.CharField('Имя', max_length=100)  # Поле для имени (как ячейка в таблице 📝)
    age = models.IntegerField('Возраст')  # Числовое поле для возраста 🔢
"""

from enum import unique
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    last_name = models.CharField(max_length=150, verbose_name="Фамилия", unique=True)


    #поля модели базы данных
    age = models.IntegerField(help_text='Введите возраст студента') #для отображенгия числе
    is_active = models.BooleanField(default=True)#является  ил студент актвным
    description = models.TextField (null=True, blank=True) #(описание) для отображения строки фиксированый длины
    created_ad = models.DateTimeField(auto_now=True) #предосталяет  дату  и вермя
    image = models.ImageField() # для хранения изображения
    # для создания поля внешнего ключа используется fotegen_key
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    STATUS_CHOICES = [('draft', 'Draft'),
                      ('publushed', 'Published')]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default = 'draft')






    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "студент"
        verbose_name_plural = 'студены'
        ordering = ["last_name"]
        db_table = 'custom_table_name'
# Create your models here.
