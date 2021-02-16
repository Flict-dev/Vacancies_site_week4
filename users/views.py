from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.base import View, TemplateView

from company.forms import CompanyForm, VacancyForm
from .forms import MyRegistrationForm
from django.shortcuts import render, redirect
from company.models import Company, Vacancy, Application


def check(request):
    try:
        Company.objects.get(owner=request.user.id)
        return render(request, 'users/company_edit.html', context={'form': CompanyForm})
    except ObjectDoesNotExist:
        return render(request, 'users/company_create.html', context={})


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
        company = Company.objects.get(owner=request.user.id)
        return render(request, 'users/company_edit.html', context={'form': CompanyForm(instance=company)})

    def post(self, request, *args, **kwargs):
        form = CompanyForm(request.POST)
        user = User(request.user)
        if form.is_valid():
            defaults = form.cleaned_data
            Company.objects.update_or_create(owner=user.id, defaults=defaults)
            return redirect('/mycompany/')
        return render(request, 'users/company_edit.html', context={'form': form})


class ProfileVacanciesView(TemplateView):
    template_name = 'users/vacancy-list.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileVacanciesView, self).get_context_data(**kwargs)
        try:
            company = Company.objects.get(owner=self.request.user.id)
            context['vacancies'] = Vacancy.objects.filter(company=company).select_related('company')
            return context
        except ObjectDoesNotExist:
            self.template_name = 'users/company_create.html'


class ProfileVacanciesEdit(View):
    def get(self, request):
        return render(request, 'users/vacancy_create.html', context={'form': VacancyForm})

    def post(self, request, *args, **kwargs):
        form = VacancyForm(request.POST)
        company = Company.objects.get(owner=self.request.user.id)
        if form.is_valid():
            form = form.cleaned_data
            Vacancy.objects.update_or_create(defaults=form, company=company)
            return redirect('/mycompany/vacancies/')
        return render(request, 'users/vacancy_create.html', context={'form': form})
