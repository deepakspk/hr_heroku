from django.urls import path, re_path, reverse
from . import views
from django.contrib import admin

app_name = 'userapp'

urlpatterns = [
    path('',views.IndexView,name='index'),
    path('profile/',views.ProfileView,name='profile'),
    path('department_list',views.DepartmentListView.as_view(),name='department_list'),
    path('empdeplist/<int:pk>/',views.ListofEmpInDep, name="empdeplist"),
    path('employee/update/',views.EmployeeUpdateView.as_view(),name='employee_update'),
]