from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from apps.users.views import RegistrationView, ActivationView

app_name = 'users'

urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('activate/<uidb64>/<token>/', ActivationView.as_view(), name='activate'),
    path('login', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]