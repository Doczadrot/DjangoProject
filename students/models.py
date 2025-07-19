
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


    YEAR_IN_SCHOOL_CHOICE = [
        (FIRST_YEAR, 'Первый курс'),
        (SECOND_YEAR, 'Второй курс'),
        (THIRD_YEAR, 'Третий курс'),
        (FOURTH_YEAR, 'Четвертый курс')
         ]

    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    email = models.EmailField()
    year = models.CharField(max_length=6, choices=YEAR_IN_SCHOOL_CHOICE,default=FIRST_YEAR, verbose_name='Курс')
    enrollment_date = models.DateField()


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
        #добавялем специальные права пользователей
        permissions = [
            ('can_promote_student', 'Разрешение на перевод студента'), #1 значение указывает право как оно будет сохранено
            ('can_expel_student', 'Разрешение на исключение студента') #2 значение это как оно будет выглядеть в командном меню
            ]