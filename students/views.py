from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'students/home.html')

def about(request):
    """
    🌟 Процесс обработки запроса как в ресторане:
    1. Клиент (браузер) → заказ (GET-запрос на /about)
    2. Менеджер (URL-роутер) → передает заказ шеф-повару (view)
    3. Шеф-повар (эта функция):
       - Берет ингредиенты (данные из БД/логики)
       - Готовит блюдо (формирует контекст)
    4. Официант (шаблон about.html) → подает HTML-страницу
    """
    return render(request, template_name='students/about.html')

def contact(request):
    if request.method == 'POST':
        # Обработка данных формы
        name = request.POST.get('name')
        email = request.POST.get('email')

        return HttpResponse(f'Спасибо, {name}! Мы скоро свяжемся с вами по {email}.')
    return render(request, template_name='students/contact.html')

