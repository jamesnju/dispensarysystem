from django.db import models

# Create your models here.
class Student(models.Model):
    studentname = models.CharField(max_length=30, null=False, blank=False)
    studentnumber=models.CharField(max_length=30, null=False, blank=False)
    email=models.CharField(max_length=50, null=False, blank=False)
    phone=models.CharField(max_length=13, null=False, blank=False)
    reisterdate=models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.studentnumber
