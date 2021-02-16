from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Vacancy(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name='Название',
    )
    speciality = models.ForeignKey(
        'Speciality',
        related_name='vacancies',
        on_delete=models.CASCADE,
    )
    company = models.ForeignKey(
        'Company',
        related_name='vacancies',
        on_delete=models.CASCADE,
    )
    skills = models.CharField(
        max_length=150,
        verbose_name='Навыки',
    )
    salary_min = models.PositiveSmallIntegerField(
        verbose_name='Мин зарплата',
    )
    salary_max = models.PositiveSmallIntegerField(
        verbose_name='Макс зарплата',
    )
    published = models.DateTimeField(
        default=datetime.now(),
        verbose_name='Опубликовано',
    )

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_vacancy', kwargs={"pk": self.pk})


class Company(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name='Название',
    )
    location = models.CharField(
        max_length=50,
        verbose_name='Город',
    )
    logo = models.ImageField(
        upload_to='images/%Y/%d/%m/',
        verbose_name='Лого',
    )
    description = models.TextField(
        max_length=2000,
        verbose_name='Информация',
    )
    employee_count = models.CharField(
        max_length=100,
        verbose_name='Кол-во сотрудников',
    )
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Владелец',
        null=True  # Убрать псоле удаления баз данных!!!
    )

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_company', kwargs={"pk": self.pk})


class Speciality(models.Model):
    code = models.CharField(
        max_length=30,
        verbose_name='Код',
    )
    title = models.CharField(
        max_length=30,
        verbose_name='Название',
    )
    image = models.ImageField(
        upload_to='images/%Y/%d/%m/',
        verbose_name='зображение',
    )

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_speciality', kwargs={"code": self.code})


class Application(models.Model):
    username = models.CharField(max_length=40, verbose_name='Имя')
    phone = models.CharField(max_length=11, verbose_name='Телефон')
    letter = models.TextField(max_length=1000, verbose_name='Письмо', default='', null=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, verbose_name='Вакансия')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'

    def __str__(self):
        return self.username
