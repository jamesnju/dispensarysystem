from django.urls import path
from .views import dispensary_list

urlpatterns = [
    path("", dispensary_list, name="dispensary_list"),
    
]
