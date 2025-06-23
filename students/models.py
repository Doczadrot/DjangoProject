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
from django.db import models# Импортируем модуль models из Django для создания моделей базы данных


class MyModel(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Определяем модель Student, которая будет представлять таблицу студентов в базе данных
class Student(models.Model):
    # Определяем константы для курсов обучения
    FIRST_YEAR = 'first'        # Константа для первого курса
    SECOND_YEAR = 'second'      # Константа для второго курса
    THIRD_YEAR = 'third'        # Константа для третьего курса
    FOURTH_YEAR = 'fourth'      # Константа для четвертого курса

    # Определяем список выбора для поля "курс"
    # Каждый элемент списка - это кортеж из двух значений:
    # 1. Значение, которое будет храниться в базе данных (например, 'first')
    # 2. Значение, которое будет отображаться пользователю (например, 'Первый курс')
    YEAR_IN_SCHOOL_CHOICE = [
        (FIRST_YEAR, 'Первый курс'),
        (SECOND_YEAR, 'Второй курс'),
        (THIRD_YEAR, 'Третий курс'),
        (FOURTH_YEAR, 'Четвертый курс')
         ]
    
    # Поле для имени студента
    # models.CharField - текстовое поле
    # max_length=150 - максимальная длина имени 150 символов
    # verbose_name='Имя' - отображаемое имя поля в админ-панели и формах
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    
    # Поле для фамилии студента
    # Аналогично полю first_name
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    
    # Поле для курса студента
    # max_length=6 - максимальная длина (с запасом для возможных значений)
    # choices=YEAR_IN_SCHOOL_CHOICE - указывает, что значения для этого поля должны выбираться из списка YEAR_IN_SCHOOL_CHOICE
    # default=FIRST_YEAR - значение по умолчанию, если курс не указан
    # verbose_name='Курс' - отображаемое имя поля
    
    year = models.CharField(max_length=6, choices=YEAR_IN_SCHOOL_CHOICE,default=FIRST_YEAR, verbose_name='Курс')


    # Метод __str__ определяет строковое представление объекта Student
    # Это то, что будет отображаться, например, в админ-панели Django при выводе списка студентов
    # Возвращает строку с именем и фамилией студента
    def __str__(self): #строковое представлени стр тут у нас будет возвращатсья имя фамиля
        return f'{self.first_name} {self.last_name} - {self.get_year_display()}'
    
    # Класс Meta содержит метаданные для модели Student
    #заданим подяок сортирвоки оп фамилии
    class Meta:
        # verbose_name - имя модели в единственном числе для отображения в админ-панели
        verbose_name = 'Студент'
        # verbose_name_plural - имя модели во множественном числе
        verbose_name_plural = 'Студенты'
        # ordering - определяет порядок сортировки записей по умолчанию
        # В данном случае, студенты будут отсортированы по фамилии (last_name)
        #порядок сортировки - значение создается как стока
        ordering = ['last_name']