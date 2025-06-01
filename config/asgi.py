"""
ASGI конфигурация для асинхронного взаимодействия ⚡

Для новичков:
Это как диспетчерская для асинхронных задач (чатов, уведомлений) 📡
- Работает с современными протоколами WebSocket
- Используется для реального времени (как живое общение по рации 📞)
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()
