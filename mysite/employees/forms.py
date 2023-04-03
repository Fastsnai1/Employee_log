from django import forms
from .models import *


class AddWorkerForm(forms.Form):
    first_name = forms.CharField(max_length=200, label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=200, label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    surname = forms.CharField(max_length=200, label='Отчество', widget=forms.TextInput(attrs={'class': 'form-control'}))
    slug = forms.SlugField(max_length=250, label='URL', widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.DateField(label='Возраст', widget=forms.DateInput())
    male_or_female = forms.ModelChoiceField(queryset=Gender.objects.all(), label='Пол')
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория')
    pos = forms.ModelChoiceField(queryset=Position.objects.all(), label='Должность')