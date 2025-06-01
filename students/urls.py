from django.urls import path
from .views import *
from students import views

app_name = 'students' #Название приложения для ссылки в navbar.html
# Создаем список маршрутов (URL)
#В urlpatterns мы указываем, что при запросе на определенный URL, какой view должен обрабатывать этот запрос.
#path() - это функция, которая принимает три аргумента:
urlpatterns = [
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact')
]