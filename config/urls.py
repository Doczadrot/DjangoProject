"""
Конфигурация URL для проекта config.

Список `urlpatterns` направляет URL к представлениям. Подробнее:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Примеры:
Функциональные представления
    1. Импортируйте: from my_app import views
    2. Добавьте URL: path('', views.home, name='home')
Класс-базированные представления
    1. Импортируйте: from other_app.views import Home
    2. Добавьте URL: path('', Home.as_view(), name='home')
Включение других URLconf
    1. Импортируйте функцию include: from django.urls import include, path
    2. Добавьте URL: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
"""
Маршрутизатор проекта - URL-диспетчер 🌐
Это как таблица содержания для всего сайта! 📖
Здесь мы связываем:
- URL-адреса (как названия глав) ➡️
- Представления (как сами страницы) 📄
Пример:
path('about/', views.about) - когда заходим на /about,
вызывается функция about из views.py
"""

from django.urls import path, include
from students import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('students/', include('students.urls', namespace='students')),
    path('contact/',views.contact, name='contact')
]