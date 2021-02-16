from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import(
    MyLoginView,
    MyRegistrationView,
    ProfileCompanyView,
    ProfileVacanciesView,
    ProfileVacanciesEdit,
    check)

urlpatterns = [
    path('profile/check/', check, name='check'),
    path('registration/', MyRegistrationView.as_view(), name='reg'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('mycompany/', ProfileCompanyView.as_view(), name='profile_company'),
    path('mycompany/vacancies/', ProfileVacanciesView.as_view(), name='profile_vacancies'),
    path('mycompany/vacancies/edit/', ProfileVacanciesEdit.as_view(), name='edit_vacancy'),
]
