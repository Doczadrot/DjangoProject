from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView, View
from students. forms import StudentForm
from students.models import Student, MyModel
from django.http import HttpResponseForbidden
from students.forms import ContactForm
from django.core.cache import cache
from .models import Student
from .services import StudentService


class PromoteStudentView(LoginRequiredMixin, View): #LoginRequiredMixin - проверяем этим методом что бы пользователь был авторизован
    def post(self, request, student_id):
        student = get_object_or_404(Student, id=student_id) #
        # Если у нашел обьекта есть право для перевода студента
        if not request.user.has_perm('student.can_promote_student'):
            return HttpResponseForbidden('У вас нет права для перевода студента') #Если нет права

        student.year = next_year(student.year)
        student.save()

        return redirect('students:student_list')

class ExpelStudentView(LoginRequiredMixin, View):  # LoginRequiredMixin - проверяем этим методом что бы пользователь был авторизован
    def post(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)  #
        # Если у нашел обьекта есть право для исключения студента
        if not request.user.has_perm('student.can_expel_student'):
            return HttpResponseForbidden('У вас нет прав для исключения')  # Если нет права

        student.delete()
        return redirect('students:student_list')


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        if not self.request.user.has_perm('students.view_student'):
            return Student.objects.none()
        return Student.objects.all()


class StudentCreateView(CreateView):
    model = Student
    #fields = ['first_name', 'last_name', 'year', 'email', 'enrollment_date']
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('students:student_list')

class StudentUpdateView(UpdateView):
    form_class = StudentForm
    model = Student
    #fields = ['first_name', 'last_name', 'year', 'email', 'enrollment_date']
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('students:student_list')



class MyModelDeleteView(DeleteView):
    model = MyModel
    template_name = 'students/mymodel_confirm_delete.html'
    success_url = reverse_lazy('students:mymodel_list')

class MyModelUpdateView(UpdateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'students/mymodel_form.html'
    success_url = reverse_lazy('students:mymodel_list')



class MyModelCreateView(CreateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'students/mymodel_form.html'
    success_url = reverse_lazy('students:mymodel_list')


class MyModelList(ListView):
    model = MyModel
    template_name = 'students/mymodel_list.html'
    context_object_name = 'mymodels'

class MyModelDetailView(DetailView):
    model = MyModel
    template_name = 'students/mymodel_detail.html'
    context_object_name = 'mymodel'



def about(request):
    return render(request, template_name='students/about.html')



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
        form = ContactForm(request.POST) # Создаем экземпляр формы с данными из POST-запроса
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Здесь вы можете отправить email или сохранить сообщение в базу данных
            # Например: send_mail('Сообщение с сайта', message, email,
            return HttpResponse(f'Спасибо, {name}! Мы скоро свяжемся с вами по {email}.')
        else:
            # Если форма недействительна, она будет отображена снова с ошибками
            pass # Нет необходимости делать что-либо, форма будет передана в шаблон
    else:
        form = ContactForm() # Создаем пустую форму для GET-запроса

    return render(request, 'students/contact.html', context={'form': form})

#обьявляем контроллер и передаем обьект http(request)
def example_view(request):
    return render(request, template_name='students/example.html')


def student_list(request): #контроллер для списка студентов всегда использует request
    students = Student.objects.all() #получаем всех студентов по id
    context = {
        'students': students}
    return render(request, template_name='students/student_list.html', context=context)

def my_view(request):
    data = cache.get('my_key')

    if not data:
        data = 'Какая то информация от куда либо'
        cache.set('my_key', data, 60 * 15)
    return HttpResponse(data)


class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html' #Шаблон
    context_object_name = 'student'

    #если нам нужно вывести доллнительный контект то нужно переопределить контект

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student_id = self.object.id # получаем тудент айти из селф


        #далее через контекст
        context['full_name'] = StudentService.get_full_name(student_id)#
        context['average_grade'] = StudentService.calculate_average(student_id)# расширяем
        context['has_passed'] = StudentService.has_passed(student_id)#

        return context




