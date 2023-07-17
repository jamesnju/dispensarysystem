""" from django.contrib.auth.backends import ModelBackend

from dispensary import forms
from .models import Student

from django.contrib.auth.forms import AuthenticationForm
from .models import Student



class CustomAuthenticationForm(AuthenticationForm):
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        try:
            student = Student.objects.get(studentnumber=username)
        except Student.DoesNotExist:
            raise forms.ValidationError('Invalid student number')

        if student.studentstatus != 'registered':
            raise forms.ValidationError('You are not registered')

        if not student.check_password(password):
            raise forms.ValidationError('Invalid password')

        return cleaned_data """


""" class StudentNumberBackend(ModelBackend):
    def authenticate(self, request, studentnumber=None, password=None, **kwargs):
        try:
            student = Student.objects.get(studentnumber=studentnumber)
        except Student.DoesNotExist:
            return None
        
        if student.check_password(password):
            return student
        
        return None
 """





"""  from django.contrib.auth.backends import BaseBackend
from dispensary.models import Student


class StudentBackend(BaseBackend):
    def authenticate(self, request, studentnumber=None, password=None):
        try:
            student = Student.objects.get(studentnumber=studentnumber)
            if student.check_password(password):
                return student
        except Student.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Student.objects.get(pk=user_id)
        except Student.DoesNotExist:
            return None
 
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class StudentBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            if '@' in username:
                # Handle email-based login
                user = User.objects.get(email=username)
            else:
                # Handle student number-based login
                user = User.objects.get(studentnumber=username)

            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
 """ 