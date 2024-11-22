

from django.urls import path
from bms_driversworkers_management import views

urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),  # Optional: Separate employee list view
    path('add_employee/', views.add_employee, name='add_employee'),
    path('employees/edit/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('employees/delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('driver_schedule/add/', views.add_driver_schedule, name='add_driver_schedule'),
    path('driver_schedule/', views.driver_schedule_list, name='driver_schedule_list'),
    path('driver_schedule/edit/<int:pk>/', views.edit_driver_schedule, name='edit_driver_schedule'),
    path('driver_schedule/delete/<int:pk>/', views.delete_driver_schedule, name='delete_driver_schedule'),
]
