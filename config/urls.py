
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
    path('admin/', admin.site.urls),
    path('', student_views.home, name='home'),  # Главная страница
    path('about/', student_views.about, name='about'),  # Страница "О нас"
    path('contact/', student_views.contact, name='contact'),  # Страница "Контакты"
    path('students/', include('students.urls', namespace='students')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

