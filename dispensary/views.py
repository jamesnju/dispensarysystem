from django.shortcuts import get_object_or_404, render
from .models import Student
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required

def dispensary_list(request):
    dispensaries = Student.objects.all()
    context = {
        "title": "Dispensary List",
        "dispensaries": dispensaries
    }
    return render(request, "dispensary/dispensary_list.html", context=context)

def per_student_view(request, pk):
    students = get_object_or_404(Student, pk=pk)
    context = {
        'students': students
    }
    return render(request, "dispensary/per_student_view.html", context=context)
