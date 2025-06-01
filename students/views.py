from django.shortcuts import render
from django.http import HttpResponse


<<<<<<< HEAD
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

=======
#обьявляем контроллер и передаем обьект http(request)
def example_view(request): 
    # Ваш код для обработки запроса
    # возвращает HttpResponse или другой объект
    #render - функция которая возвращает html страницу 
    # и отправляем путь до шаблона
    return render(request, 'example.html')

#пишем контроллер обрабатыващий различные запросы
#(Контроллер всегдаспользует (request))
def show_data(request):
    if request.method == "GET":  # Check if request method is GET
        return render(request, template_name='example.html')

def show_data(request):
    if request.method == "POST":  # Check if request method is GET
        return HttpResponse("Data sent successfully")
>>>>>>> 4c8d661fcdde86047e12f8fe9ea8ab23506eab11
