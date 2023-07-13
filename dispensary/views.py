from django.shortcuts import get_object_or_404, redirect, render
from .models import Student
from django.contrib.auth.decorators import login_required
from .forms import AddStudentForm, UpdateStudentForm
from django.contrib import messages
# Create your views here.

@login_required

def dispensary_list(request):
    dispensaries = Student.objects.all()
    context = {
        "title": "Dispensary List",
        "dispensaries": dispensaries
    }
    return render(request, "dispensary/dispensary_list.html", context=context)
@login_required
def per_student_view(request, pk):
    students = get_object_or_404(Student, pk=pk)
    context = {
        'students': students
    }
    return render(request, "dispensary/per_student_view.html", context=context)
@login_required
def addstudent(request):
    if request.method == "POST":
        add_form =AddStudentForm(data=request.POST)
        if add_form.is_valid():
            new_students = add_form.save(commit=True)
            new_students.save()
            messages.success(request,"Student successfully added")
            return redirect("/dispensary/")
    else:
            add_form = AddStudentForm()
    return render(request, "dispensary/studentadd.html", {"form": add_form})

@login_required
def deletestudent(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    messages.success(request, "student detailes deleted")
    return redirect("/dispensary/")
@login_required
def UpdateStudentdetails(request, pk):
    students = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        UpdateForm = UpdateStudentForm(data=request.POST)
        if UpdateForm.is_valid():
            students.studentname = UpdateForm.data['studentname']
            students.studentnumber =UpdateForm.data['studentnumber']
            students.email=UpdateForm.data['email']
            students.phone=UpdateForm.data['phone']
            students.save()
            messages.success(request, "studented details successfully updated")
            return redirect(f"/dispensary/details/{pk}")
        
    else:
        UpdateForm=UpdateStudentForm(instance=students)
    context = {"form": UpdateForm}
    return render(request, "dispensary/studentupdate.html", context=context)


          

