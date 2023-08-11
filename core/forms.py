from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User

from core import models


class HomeForm(forms.ModelForm):

    def clean_name(self):
        num = self.cleaned_data['num']
        if not num.isdigit():
            raise forms.ValidationError('В номерах можно использовать только цифры!')
        return num

    def clean_surname(self):
        city = self.cleaned_data['city']
        if city.isdigit():
            raise forms.ValidationError('Некорректное название города')
        return city

    class Meta:
        model = models.Home
        fields = '__all__'
