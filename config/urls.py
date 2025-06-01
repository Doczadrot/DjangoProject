"""
<<<<<<< HEAD
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
=======
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
>>>>>>> 4c8d661fcdde86047e12f8fe9ea8ab23506eab11
