from django.db import models
class Disp(models.Model):
    studentname = models.CharField(max_length=30, null=False, blank=False)
    studentnumber=models.CharField(max_length=30)
    email=models.CharField(max_length=50, null=False, blank=False)
    phone=models.CharField(max_length=13, null=False, blank=False)
    reisterdate=models.DateField(auto_now_add=True)
    reason_for_visit = models.TextField(null=True, default='')
    studentstatus = models.CharField(max_length=20, choices=[('registered', 'Registered'), ('not_registered', 'Not Registered')])
    password = models.CharField(max_length=100, default='')
    

    def __str__(self) -> str:
        return self.studentnumber