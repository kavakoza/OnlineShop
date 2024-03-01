from django.urls import path
from users.apps import UsersConfig
from users.views import RegistrationView, LoginView, registration_success, LogoutView, ProfileView

app_name = UsersConfig.name

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('registration_success/', registration_success, name='registration_success'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(http_method_names=['post', 'get', 'options']), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile')
]
