from django import forms
from products.models import Product


class ProductForm(forms.ModelForm):
    """
    Product form creation
    """
    class Meta:
        model = Product
        exclude = ('seller',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Add name here',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 5, 'placeholder': 'Add description here',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
        }

    def __check(self, field):
        """
        Checking words in fields
        """
        prohibited_words = ['free', 'casino', 'scam']
        cleaned_data = self.cleaned_data[field]
        for word in prohibited_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'The field contains one of prohibited words - "{word}". '
                                            f'Please replace them and try again.')
        return cleaned_data

    def clean_name(self):
        return self.__check('name')

    def clean_description(self):
        return self.__check('description')
