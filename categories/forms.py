from django import forms
from django.core.exceptions import ValidationError
from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'category name', 'class': 'block text-sm font-medium text-gray-700'}),
            'description': forms.Textarea(attrs={'placeholder': 'enter category description', 'rows': 2,
                                                 'class': 'block text-sm font-medium text-gray-700'}),
            'image': forms.FileInput(attrs={'accept': 'image/*', 'class': 'block text-sm font-medium text-gray-700'})
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.isalpha():
            raise ValidationError('Name must contain only letters.')
        return name

