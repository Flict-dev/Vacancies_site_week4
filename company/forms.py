from crispy_forms.bootstrap import AppendedText, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from django import forms
from django.forms import ModelForm

from .models import Application, Vacancy, Company


class ApplicationForm(forms.Form):
    username = forms.CharField(max_length=40, label='Имя')
    phone = forms.CharField(max_length=11, label='Телефон')
    letter = forms.CharField(max_length=1500, widget=forms.Textarea, required=False, label='Письмо')

    class Meta:
        fields = ['username', 'phone', 'letter']


class CompanyForm(ModelForm):
    logo = forms.ImageField(required=False)

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
