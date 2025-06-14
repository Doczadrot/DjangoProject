"""

WSGI конфигурация - основа для работы приложения 🏗️

Для новичков:
Это фундамент, который:
- Запускает Django (как стартовая кнопка двигателя 🚀)
- Обрабатывает обычные HTTP-запросы (как классическая почта 📨)
- Работает с синхронными задачами

WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
