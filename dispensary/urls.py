from django.urls import path
from django.urls import path, include
from .views import UpdateStudentdetails, deletestudent, dispensary_list, not_registered, per_student_view,addstudent
from dispensary import views


urlpatterns = [
    path("", views.index, name="index"),
    path("not_registered/", not_registered, name="not_registered"),
    path("list/", dispensary_list, name="dispensary_list"),
    path("details/<int:pk>", per_student_view, name="per_student_view"), 
    path("studentadd/", addstudent, name="Addstudent"),
    path("delete/<int:pk>", deletestudent, name="deletestudent" ),
    path("UpdateStudent/<int:pk>",UpdateStudentdetails, name="UpdateStudentdetails"),
]
