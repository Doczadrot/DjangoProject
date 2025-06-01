"""
<<<<<<< HEAD
ASGI конфигурация для асинхронного взаимодействия ⚡

Для новичков:
Это как диспетчерская для асинхронных задач (чатов, уведомлений) 📡
- Работает с современными протоколами WebSocket
- Используется для реального времени (как живое общение по рации 📞)
=======
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
>>>>>>> 4c8d661fcdde86047e12f8fe9ea8ab23506eab11
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()
