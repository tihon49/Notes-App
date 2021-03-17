from django import forms
from .models import *


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        """валидация формы"""

        cleaned_data = super().clean()
        new_name = self.cleaned_data['name']

        if not new_name:
            print('Пустое')
            raise forms.ValidationError('Введите название заметки')
        if len(new_name) > 40:
            print('Больше 40-ка')
            raise forms.ValidationError('Слишком длинное название')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'count', 'value']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'название продукта'}),
            'count': forms.NumberInput(attrs={'class': 'form-control',
                                              'placeholder': 'кол-во'}),
            'value': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {'name': 'название продукта',
                  'count': 'количество',
                  'value': 'величина'}
