# weather/forms.py
from django import forms

class CityForm(forms.Form):
    city = forms.CharField(max_length=100, label='Город', widget=forms.TextInput(attrs={
        'placeholder': 'Введите название города',
        'label': 'Город',
    }))