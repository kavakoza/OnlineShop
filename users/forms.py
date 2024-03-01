from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User


class UserRegistrationForm(UserCreationForm):
    """
    User registration form
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):
    """
    User profile form
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number', 'avatar', 'country')


class UserLoginForm(AuthenticationForm):
    """
    User login form
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
