from django import forms
from .models import Registro
from .models import login

class  RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = '__all__'

class  LoginForm(forms.ModelForm):
    class Meta:
        model = login
        fields = '__all__'