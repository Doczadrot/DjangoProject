from django.db import models # Импортируем модуль models из Django для создания моделей базы данных

class Student(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    birth_date = models.DateField(null=True, blank=True)

    # Определяем константы для курсов обучения
    FIRST_YEAR = 'first'
    SECOND_YEAR = 'second'
    THIRD_YEAR = 'third'
    FOURTH_YEAR = 'fourth'

    YEAR_IN_SCHOOL_CHOICE = [
        (FIRST_YEAR, 'Первый курс'),
        (SECOND_YEAR, 'Второй курс'),
        (THIRD_YEAR, 'Третий курс'),
        (FOURTH_YEAR, 'Четвертый курс')
    ]

    email = models.EmailField(null=True, blank=True) # Добавляем поле email
    year = models.CharField(max_length=6, choices=YEAR_IN_SCHOOL_CHOICE, default=FIRST_YEAR, verbose_name='Курс', null=True, blank=True) # Добавляем поле year
    enrollment_date = models.DateField(null=True, blank=True) # Добавляем поле enrollment_date

    def __str__(self):
        # Используем get_year_display() для получения читаемого названия курса
        # Проверяем, существует ли поле 'year' у объекта перед вызовом get_year_display()
        if hasattr(self, 'year') and self.year:
            return f'{self.first_name} {self.last_name} - {self.get_year_display()}'
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['last_name']
        permissions = [
            ('can_promote_student', 'Разрешение на перевод студента'),
            ('can_expel_student', 'Разрешение на исключение студента')
        ]


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100) #Предмет
    score = models.FloatField() #cчет - ИСПРАВЛЕНО: нужны скобки ()

    def __str__(self):
        return f'{self.subject} {self.score}'


class MyModel(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name