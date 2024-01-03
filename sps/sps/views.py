#from django.urls import HttpResponse
from django.shortcuts import render, redirect

def home(request):
   return render (request, "home.html", {})

# def students_data(request):
#     return render (request, "students/students_data.html", {})

# def add_students(request):
#     return render (request, "students/home.html", {})
