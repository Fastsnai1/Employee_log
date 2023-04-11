from django import forms
from .models import *


class AddWorkerForm(forms.ModelForm):
    class Meta:
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['cat'].empty_lable = 'Категория не выбрана'

        model = Worker
        fields = ['first_name', 'last_name', 'surname', 'slug', 'age', 'male_or_female', 'cat', 'pos']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'cat': forms.Select(attrs={'class': "form-select"}),
            'pos': forms.Select(attrs={'class': "form-select"}),
            'male_or_female': forms.Select(attrs={'class': "form-select"}),
            'age': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class AddPositionForm(forms.ModelForm):
    # форма связанная с моделью
    class Meta:
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['cat'].empty_lable = 'Категория не выбрана'

        model = Position
        fields = ['name', 'cat', 'slug']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'cat': forms.Select(attrs={'class': "form-select"}),
        }

