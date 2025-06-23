
"""
Административный интерфейс приложения 🎛️

Для новичков:
Это как панель управления для ваших моделей! 📋
Здесь можно:
- Регистрировать модели (как добавлять новые разделы в админку)
- Настраивать отображение данных (как расставлять мебель в комнате 🪑)
- Добавлять фильтры и поиск (как органайзер для данных 🔍)
"""
from django.contrib import admin
from .models import  MyModel

from .models import Student

admin.site.register(Student)
admin.site.register(MyModel)
