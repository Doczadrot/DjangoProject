from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def home(request):
    student = Student.objects.filter(year='first').first()
    if student:
        context = {
            'student_name': f'{student.first_name} {student.last_name}',
            'student_year': student.get_year_display(),
        }
    else:
        context = {
            'student_name': 'Студент не найден',
            'student_year': 'Первый курс',
        }
    return render(request, template_name='students/home.html', context=context)


def student_datail(request):
    student = Student.objects.get(id=1)
    context = {
            'student': student,
        }
    return render(request, template_name='students/student_datail.html', context=context)


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

#обьявляем контроллер и передаем обьект http(request)
def example_view(request): 
    # Ваш код для обработки запроса
    # возвращает HttpResponse или другой объект
    #render - функция которая возвращает html страницу 
    # и отправляем путь до шаблона
    return render(request, template_name='students/example.html')

#пишем контроллер обрабатыващий различные запросы
#(Контроллер всегдаспользует (request))
# def show_data(request):
#     if request.method == "GET":  # Check if request method is GET
#         return render(request, template_name='example.html')
#cозздаем контроллер для вариации показа туденктов на хтмл странице
def student_list(request): #контроллер для списка студентов всегда использует request
    students = Student.objects.all() #получаем все студентов из бд
    context = {
        'students': students
    }
    return render(request, template_name='students/student_list.html', context=context)