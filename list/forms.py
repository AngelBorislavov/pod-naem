from django import forms
from .models import Rent

class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ['client_name', 'item', 'queantity', 'price', 'tel_number', 'return_date']
        labels = {
            'client_name': 'Име',
            'item': 'Артикул',
            'queantity': 'Количество',
            'price': 'Цена',
            'tel_number': 'Телефон',
            'return_date': 'Дата на връщане',
        }
        widgets = {
            'return_date': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d',
            ),
        }