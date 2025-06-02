#!/usr/bin/env python

"""
Утилита командной строки Django для административных задач. 🛠️

Для новичков:
Это как главный пульт управления проектом! Отсюда можно:
- Запускать сервер (как включить двигатель 🚀)
- Создавать приложения (как новые комнаты в доме 🏠)
- Работать с базой данных (как организовать шкаф с документами 📁)

Пример использования: python manage.py runserver
"""

"""Django's command-line utility for administrative tasks."""

import os
import sys


def main():

    """Выполнение административных задач."""

    """Run administrative tasks."""

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(

            "Не удалось импортировать Django. Убедитесь, что он установлен и "
            "доступен в переменной окружения PYTHONPATH. Возможно, вы "
            "забыли активировать виртуальное окружение?"

            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"

        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
