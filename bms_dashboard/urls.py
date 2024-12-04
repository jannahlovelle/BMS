from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('get_bus_data/', views.get_bus_data, name='get_bus_data'),
    path('get_employee_data/', views.get_employee_data, name='get_employee_data'),
    path('get_bus_schedule_history/', views.get_bus_schedule_history, name='get_bus_schedule_history'),
]