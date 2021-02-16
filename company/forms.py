from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms import ModelForm

from .models import Application, Vacancy, Company


class ApplicationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))

    username = forms.CharField(max_length=40)
    phone = forms.CharField(max_length=11)
    letter = forms.CharField(max_length=1000, required=False)

    class Meta:
        model = Application
        fields = ['username', 'phone', 'letter']


class CompanyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))

    logo = forms.ImageField(required=False)

    class Meta:
        model = Company
        fields = ['title', 'location', 'logo', 'description', 'employee_count']


class VacancyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))

    class Meta:
        model = Vacancy
        fields = ['title', 'speciality', 'skills', 'salary_min', 'salary_max', 'published']
        labels = {
            'title': 'Название вакансии',
            'speciality': 'Специализация',
            'skills': 'Навыки',
            'salary_min': 'Зарплата от',
            'salary_max': 'Зарплата до',
            'published': 'Опубликовано'
        }
