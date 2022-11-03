from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.GetAllEmployees),
    path('GetEmployeeById/<int:pk>',views.one_data),
    path('AddEmp/',views.create_data),
    path('UpdateEmp/<int:pk>',views.update_data),
    path('DeleteEmp/<int:pk>',views.delete_data),
]