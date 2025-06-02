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

from django.db import models



class Student(models.Model):
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
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    yers = models.CharField(max_length=6, choices=YEAR_IN_SCHOOL_CHOICE,default=FIRST_YEAR, verbose_name='Курс')


    def __str__(self): #строковое представлени стр тут у нас будет возвращатсья имя фамиля
        return f'{self.firs_name} {self.last_name}'
    #заданим подяок сортирвоки оп фамилии
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        #порядок сортировки - значение создается как стока
        ordering = ['last_name']




#     first_name = models.CharField(max_length=150, verbose_name="Имя")
#     last_name = models.CharField(max_length=150, verbose_name="Фамилия")
#
#
#     #поля модели базы данных
#     age = models.IntegerField(help_text = 'Введите возраст студента') #для отображенгия числе
#     is_active = models.BooleanField(default=True)#является  ил студент актвным
#     description = models.TextField (null=True, blank=True) #(описание) для отображения строки фиксированый длины
#     created_ad = models.DateTimeField() #предосталяет  дату  и вермя
#     image = models.ImageField() # для хранения изображения
#     # для создания поля внешнего ключа используется fotegen_key
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
#     tags = models.ManyToManyField(Tag)
#
#     STATUS_CHOICES = [('draft', 'Draft'),
#                       ('publushed', 'Published')]
#
#     status = models.CharField(max_length=10)
#
#
#
#
#
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'
#
#     class Meta:
#         verbose_name = "студент"
#         verbose_name_plural = 'студены'
#         ordering = ["last_name"]
#         db_table = 'custom_table_name'
# # Create your models here.
