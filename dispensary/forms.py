from django import forms
from  django.forms import ModelForm

from .models import Disp

class Registered(forms.Form):
    class Meta:
        model = Disp
        fields = ['studentnumber', 'password']

    """ studentnumber = forms.CharField(max_length=30)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

 """
class AddStudentForm(ModelForm):
    class Meta:
        model = Disp
        fields = ['studentname', 'studentnumber', 'email', 'phone']


class UpdateStudentForm(ModelForm):
    class Meta:
        model = Disp
        fields = ['studentname','studentnumber','email','phone']

