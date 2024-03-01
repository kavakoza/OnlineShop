from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from users.forms import UserRegistrationForm, UserProfileForm, UserLoginForm
from users.models import User


class RegistrationView(CreateView):
    """
    User registration
    """
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration_form.html'
    success_url = reverse_lazy('users:registration_success')


class LoginView(BaseLoginView):
    """
    Login
    """
    model = User
    template_name = 'users/login_form.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('categories:category_list')


class LogoutView(BaseLogoutView):
    """
    Logout
    """
    model = User
    template_name = 'users/login_form.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('categories:category_list')


def registration_success(request):
    """
    Successful registration
    """
    return render(request, template_name='users/registration_success.html')


class ProfileView(UpdateView):
    """
    User profile
    """
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile_form.html'
    success_url = reverse_lazy('categories:category_list')

    def get_object(self, queryset=None):
        return self.request.user
