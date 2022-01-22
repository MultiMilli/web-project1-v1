from .models import Users
from django.forms import ModelForm, TextInput

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['name']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Поле для введення'
            })
        }