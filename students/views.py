from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Student, MyModel
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy




class MyModelCreateView(CreateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'students/mymodel_form.html'
    success_url = reverse_lazy('students:mymodel_list')


class MyModelList(ListView):
    model = MyModel
    template_name = 'student/mymodel_list.html'
    context_object_name = 'mymodels'

def about(request):
    return render(request, template_name='student/about.html')



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


def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    context = {
            'student': student,
        }
    return render(request, template_name='students/student_detail.html', context=context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        return HttpResponse(f'Спасибо, {name}! Мы скоро свяжемся с вами по {email}.')
    return render(request, template_name='students/contact.html')

#обьявляем контроллер и передаем обьект http(request)
def example_view(request): 
    return render(request, template_name='students/example.html')


def student_list(request): #контроллер для списка студентов всегда использует request
    students = Student.objects.all() #получаем всех студентов по id
    context = {
        'students': students}
    return render(request, template_name='students/student_list.html', context=context)


