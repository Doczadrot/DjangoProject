# forms.py

from django import forms
from .models import Student
from django.core.exceptions import ValidationError


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # Включаем все поля из полной модели Student
        fields = ['first_name', 'last_name', 'birth_date', 'year', 'email', 'enrollment_date']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите имя'
            })

        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите фамилию'
        })

        # Раскомментируем и добавим настройки для этих полей
        self.fields['birth_date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'ГГГГ-ММ-ДД'
        })
        self.fields['year'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите курс'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите емайл'
        })
        self.fields['enrollment_date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'ГГГГ-ММ-ДД'
        })

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not email.endswith('@example.com'): # Проверяем email, только если он есть
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