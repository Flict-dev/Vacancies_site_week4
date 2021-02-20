from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Vacancy, Company, Resume


class ApplicationForm(forms.Form):
    username = forms.CharField(max_length=40, label='Имя')
    phone = forms.CharField(max_length=11, label='Телефон')
    letter = forms.CharField(max_length=1500, widget=forms.Textarea, required=False, label='Письмо')

    class Meta:
        fields = ['username', 'phone', 'letter']


class CompanyForm(ModelForm):
    logo = forms.FileField(
        label='Загрузить',
        required=False,
        widget=forms.FileInput(attrs={'class': 'custom-file-input'}),
    )

    class Meta:
        model = Company
        fields = ['title', 'location', 'logo', 'description', 'employee_count']


class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'speciality', 'skills', 'salary_min', 'salary_max']
        labels = {
            'title': 'Название вакансии',
            'speciality': 'Специализация',
            'skills': 'Навыки',
            'salary_min': 'Зарплата от',
            'salary_max': 'Зарплата до',
        }


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = [
            'name',
            'surname',
            'status',
            'salary',
            'speciality',
            'grade',
            'education',
            'experience',
            'portfolio',
        ]
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'speciality': 'Специализация',
            'status': ' Статус',
            'grade': 'Зарплата',
            'education': 'Образование',
            'experience': 'Опыт работы',
            'portfolio': 'Портфолио',
        }


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Почта',
        }


class ChangePasswordForm(forms.Form):
    password_now = forms.CharField(widget=forms.PasswordInput())
    password_new = forms.CharField(widget=forms.PasswordInput())
    class Meta:

        fields = ['password_now', 'password_new']
        labels = {
            'password_now': 'Текущий пароль',
            'password_new': 'Новый пароль',
        }