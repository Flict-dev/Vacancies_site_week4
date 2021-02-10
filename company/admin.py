from django.contrib import admin
from .models import Vacancy, Company, Speciality


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'speciality',
        'company',
        'skills',
        'salary_min',
        'salary_max',
        'published',
    ]
    list_display_links = [
        'title',
    ]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'location',
        'logo',
        'description',
        'employee_count',
    ]
    list_display_links = [
        'title',
    ]


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'code',
        'image',
    ]
    list_display_links = [
        'title',
    ]
