from django import  forms
from .models import Student
from django.core.exceptions import ValidationError


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'year', 'email', 'enrollment_date']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите имя'  # Текст подсказки внутри поля
            })

        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите фамилию'  # Текст подсказки внутри поля
        })

        self.fields['year'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите курс'  # Текст подсказки внутри поля
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите емайл'  # Текст подсказки внутри поля
        })

        self.fields['enrollment_date'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Дата'  # Текст подсказки внутри поля
        })

    def clean_email(self):
        email = self.cleaned_data.get('email') #получаем значения через гет
        if not email.endswith('@example.com'):
            raise ValidationError ('Email должен заканчиваться на @example.com')
        return email

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name and last_name and first_name == last_name:
            self.add_error('last_name', 'Имя и фамилия не могут быть одинаковыми.')
        return cleaned_data

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ваше имя")
    email = forms.EmailField(label="Ваш Email")
    message = forms.CharField(widget=forms.Textarea, label="Ваше сообщение")