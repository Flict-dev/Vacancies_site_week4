from django.shortcuts import render
from django.views.generic.base import View
from .models import Company, Vacancy, Speciality


class MainView(View):
    def get(self, request):
        specialities = Speciality.objects.all()
        companies = Company.objects.all()
        context = {
            'title': 'Main',
            'specialities': specialities,
            'companies': companies,
        }
        return render(request, 'main/index.html', context)


class DetailCompany(View):
    def get(self, request, pk):
        company = Company.objects.get(pk=pk)
        vacancies = Vacancy.objects.filter(company=company)
        context = {
            'title': company.title,
            'vacancies': vacancies,
            'company': company
        }
        return render(request, 'main/detail_company.html', context)


class DetailVacancy(View):
    def get(self, request, pk):
        vacancy = Vacancy.objects.get(pk=pk)
        context = {
            'title': vacancy.title,
            'vacancy': vacancy,
        }
        return render(request, 'main/detail_vacancy.html', context)


class DetailSpeciality(View):
    def get(self, request, code):
        speciality = Speciality.objects.get(code=code)
        vacancies = Vacancy.objects.filter(speciality=speciality)
        count_vacancy = vacancies.count()
        context = {
            'title': speciality.title,
            'vacancies': vacancies,
            'speciality': speciality,
            'count_vacancy': count_vacancy
        }
        return render(request, 'main/detail_vacancies.html', context)


class VacanciesView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        context = {
            'title': 'Vacancies',
            'vacancies': vacancies
        }
        return render(request, 'main/vacancies.html', context)