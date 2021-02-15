from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import MyRegistrationView, MyLoginView, ProfileView

urlpatterns = [
    path('registration/', MyRegistrationView.as_view(), name='reg'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/<str:username>/', ProfileView.as_view(), name='profile'),
]
