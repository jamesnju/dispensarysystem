from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import AddStudentForm, Registered, UpdateStudentForm
from django.contrib import messages
# Create your views here.
from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Disp
def index(request):
    if request.method == 'POST':
        student_number = request.POST.get('studentnumber')
        password = request.POST.get('password')

        try:
            student = Disp.objects.get(studentnumber=student_number)
        except Disp.DoesNotExist:
            student = None

        if student is not None and student.password == password:
            if student.studentstatus == 'registered':
                # User is registered, redirect to home
                messages.success(request,"successfully logged in")
                return redirect("/dispensary/list/")
            else:
                # User is not registered
                messages.success(request,"You are not registered because you are not on session")
                return render(request, 'dispensary/not_registered.html')

        # Password is incorrect or student doesn't exist
        messages.success(request,"Invalid credentials, PLease try Again")
        return render(request, 'dispensary/index.html')

    return render(request, 'dispensary/index.html')



def not_registered(request):

    return redirect(request, "not_registered.html")

@login_required
def dispensary_list(request):
    dispensaries = Disp.objects.all()
    context = {
        "title": "Dispensary List",
        "dispensaries": dispensaries
    }
    return render(request, "dispensary/dispensary_list.html", context=context)
@login_required
def per_student_view(request, pk):
    students = get_object_or_404(Disp, pk=pk)
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
    student = get_object_or_404(Disp, pk=pk)
    student.delete()
    messages.success(request, "student detailes deleted")
    return redirect("/dispensary/")
@login_required
def UpdateStudentdetails(request, pk):
    students = get_object_or_404(Disp, pk=pk)
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


          

