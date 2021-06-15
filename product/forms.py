from django import forms

from product.models import Order


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'user_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Пота'}),
            'user_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}),
            'user_message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Сообщение'}),
        }

