from django.contrib import admin
from django.urls import path
from .views import*

urlpatterns = [
    path('home/', students_home),
    path('students_data/', students_data),
    path('add_students/', add_students),
    path('delete-student/<int:student_id>', delete_student),
    path('update-student/<int:student_id>', update_student),
    path('do-update/<int:student_id>', do_update),
    
]