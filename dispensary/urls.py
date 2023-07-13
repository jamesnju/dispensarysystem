from django.urls import path
from .views import UpdateStudentdetails, deletestudent, dispensary_list,per_student_view,addstudent

urlpatterns = [
    path("", dispensary_list, name="dispensary_list"),
    path("details/<int:pk>", per_student_view, name="per_student_view"), 
    path("studentadd/", addstudent, name="Addstudent"),
    path("delete/<int:pk>", deletestudent, name="deletestudent" ),
    path("UpdateStudent/<int:pk>",UpdateStudentdetails, name="UpdateStudentdetails"),
]
