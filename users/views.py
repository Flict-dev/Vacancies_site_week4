from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from django.views.generic.base import View
from company.forms import CompanyForm, VacancyForm
from .forms import MyRegistrationForm
from django.shortcuts import render, redirect
from company.models import Company, Vacancy, Application


def check(request):
    try:
        Company.objects.get(owner=request.user.id)
        return redirect('/mycompany/')
    except ObjectDoesNotExist:
        return render(request, 'company/company_check.html', context={})


class MyRegistrationView(View):
    def get(self, request):
        return render(request, 'users/registration.html', context={'form': MyRegistrationForm})

    def post(self, request, *args, **kwargs):
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        return render(request, 'users/registration.html', context={'form': form})


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'users/login.html'


class ProfileCompanyView(View):
    def get(self, request):
        try:
            company = Company.objects.get(owner=request.user.id)
            return render(request, 'company/company_edit.html', context={'form': CompanyForm(instance=company)})
        except ObjectDoesNotExist:
            return render(request, 'company/company_edit.html', context={'form': CompanyForm()})

    def post(self, request, *args, **kwargs):
        form = CompanyForm(request.POST)
        user = User(request.user)
        if form.is_valid():
            defaults = form.cleaned_data
            Company.objects.update_or_create(owner=user.id, defaults=defaults)
            return redirect('/mycompany/vacancies/')
        return render(request, 'company/company_edit.html', context={'form': form})


class ProfileVacanciesView(View):
    def get(self, request):
        try:
            company = Company.objects.get(owner=self.request.user.id)
            context = {
                'vacancies': Vacancy.objects.filter(company=company).annotate(app_count=Count('application'))
            }
            return render(request, 'vacancy/vacancy-list.html', context=context)
        except ObjectDoesNotExist:
            return redirect('/profile/check/')


class ProfileVacanciesEdit(View):
    def get(self, request, pk):
        vacancy = Vacancy.objects.get(pk=pk)
        applications = Application.objects.filter(vacancy=vacancy)
        context = {
            'title': vacancy.title,
            'form': VacancyForm(instance=vacancy),
            'applications': applications
        }
        return render(request, 'vacancy/vacancy_edit.html', context=context)

    def post(self, request, *args, **kwargs):
        form = VacancyForm(request.POST)
        company = Company.objects.get(owner=self.request.user.id)
        if form.is_valid():
            form = form.cleaned_data
            Vacancy.objects.update_or_create(defaults=form, company=company)
            return redirect('/mycompany/vacancies/')
        return render(request, 'vacancy/vacancy_edit.html', context={'form': form})


class ProfileVacanciesCreate(View):
    def get(self, request):
        return render(request, 'vacancy/vacancy_create.html', context={'form': VacancyForm})

    def post(self, request, *args, **kwargs):
        form = VacancyForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            speciality = form.cleaned_data['speciality']
            company = Company.objects.get(owner=self.request.user.id)
            skills = form.cleaned_data['skills']
            salary_min = form.cleaned_data['salary_min']
            salary_max = form.cleaned_data['salary_max']
            Vacancy.objects.create(
                title=title,
                speciality=speciality,
                company=company,
                skills=skills,
                salary_min=salary_min,
                salary_max=salary_max,
            )
            return redirect('/mycompany/vacancies/')
        return render(request, 'vacancy/vacancy_create.html', context={'form': form})
