from django.contrib import admin

from .models import Vacancy, Company, Speciality, Application


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'speciality',
        'company',
        'skills',
        'salary_min',
        'salary_max',
        'published',
    )
    list_filter = ('speciality', 'company', 'published')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'location',
        'logo',
        'description',
        'employee_count',
    )


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'title', 'image')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'phone', 'letter', 'vacancy', 'user')
    list_filter = ('vacancy', 'user')
