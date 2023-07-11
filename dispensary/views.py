from django.shortcuts import render
from .models import Student
# Create your views here.
def dispensary_list(request):
    dispensaries = Student.objects.all()
    context = {
        "title": "Dispensary List",
        "dispensaries": "dispensaries"
    }
    return render(request, "dispensary/dispensary_list.html", context=context)
