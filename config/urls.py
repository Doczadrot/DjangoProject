"""
Конфигурация URL для проекта config.

Это главный файл URL-маршрутизации вашего Django проекта. 🚦
Он как диспетчер на вокзале, который говорит, по какому пути
отправить запрос пользователя, чтобы он попал в нужное место (представление).

Список `urlpatterns` направляет URL к представлениям (views).
Подробнее можно почитать тут:
    https://docs.djangoproject.com/en/stable/topics/http/urls/

Основные моменты:
1. `from django.urls import path, include`: Импортируем нужные инструменты.
   `path` - для создания простого маршрута.
   `include` - для подключения маршрутов из других приложений (как папки с файлами).

2. `from students import views`: Если у вас есть представления прямо в этом приложении
   (хотя обычно они в своих приложениях, как `students.views`).

3. `urlpatterns = [...]`: Список всех маршрутов вашего сайта.
   Каждый `path(...)` - это отдельный маршрут.

Примеры:
- `path('admin/', admin.site.urls)`: Стандартный маршрут для админ-панели Django. 🎩
- `path('', views.home, name='home')`: Маршрут для главной страницы.
  - Первый аргумент (`''`) - это сам URL (пустая строка означает корень сайта).
  - Второй аргумент (`views.home`) - функция-представление, которая обработает этот URL.
  - Третий аргумент (`name='home'`) - имя маршрута, чтобы на него можно было ссылаться в шаблонах и коде.
- `path('students/', include('students.urls', namespace='students'))`:
  Подключает все URL-адреса из приложения `students` (из файла `students/urls.py`).
  Все URL из `students.urls` будут начинаться с `students/` (например, `students/list/`).
  `namespace='students'` помогает избегать конфликтов имен маршрутов между приложениями.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# Импортируем представления из приложения students, если они используются напрямую в этом файле
# Если у вас есть представления home, about, contact в config/views.py, то импорт должен быть таким:
# from . import views # или from config import views
# Но судя по структуре, они скорее всего в students/views.py или других приложениях.
# Для примера ниже, я предполагаю, что views.home, views.about, views.contact находятся в students.views
from students import views as student_views # Используем псевдоним, чтобы было понятнее

urlpatterns = [
    # Маршрут для админ-панели Django
    path('admin/', admin.site.urls),

    # Маршруты для основных страниц сайта
    # Предполагаем, что эти представления (home, about, contact) находятся в students/views.py
    # Если они в другом месте, нужно будет скорректировать импорт и вызов
    path('', student_views.home, name='home'),  # Главная страница
    path('about/', student_views.about, name='about'),  # Страница "О нас"
    path('contact/', student_views.contact, name='contact'),  # Страница "Контакты"

    # Подключение URL-маршрутов из приложения 'students'
    # Все URL, определенные в students/urls.py, будут доступны по префиксу 'students/'
    # Например, если в students/urls.py есть path('all/', ...), то полный URL будет 'students/all/'
    path('students/', include('students.urls', namespace='students')),

    # Сюда можно добавлять другие маршруты для других приложений или страниц
    # path('blog/', include('blog.urls', namespace='blog')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

