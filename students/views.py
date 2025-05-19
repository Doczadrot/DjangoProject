from django.shortcuts import render
from django.http import HttpResponse


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
