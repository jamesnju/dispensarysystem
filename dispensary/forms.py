from  django.forms import ModelForm
from .models import Student

class AddStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['studentname', 'studentnumber', 'email', 'phone']


class UpdateStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['studentname','studentnumber','email','phone']
