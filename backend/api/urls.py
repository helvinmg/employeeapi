from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('employees/',views.emp_all,name='emp_all'),
    path('employees/<int:id>/',views.emp_one,name='emp_one'),
    path('employees/create/',views.emp_create,name='emp_create'),
]
