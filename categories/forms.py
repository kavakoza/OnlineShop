from django import forms
from categories.models import Category


class CategoryCreateForm(forms.ModelForm):
    """
    Category creation form
    """
    class Meta:
        model = Category
        fields = ('name', 'description', 'image')
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Title'}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Description'}
            ),
            'image': forms.ClearableFileInput(
                attrs={'class': 'form-control'}
            )
        }
        labels = {
            'name': '',
            'description': '',
        }
