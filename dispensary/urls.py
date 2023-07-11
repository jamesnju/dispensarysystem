from django.urls import path
from .views import dispensary_list,per_student_view

urlpatterns = [
    path("", dispensary_list, name="dispensary_list"),
    path("details/<int:pk>", per_student_view, name="per_student_view"),   
]
