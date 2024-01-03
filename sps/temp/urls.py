# from django.contrib import admin
from django.urls import path
# from . import views
from .views import temp_home, tempData

urlpatterns = [
    path('temp_home/', temp_home),    
    path('tempData/', tempData)
]