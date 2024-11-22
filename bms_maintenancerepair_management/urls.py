

from django.urls import path
from bms_maintenancerepair_management import views

urlpatterns =[
    path('add_repair/', views.add_repair, name='add_repair'),
    path('edit_repair/<int:pk>/', views.edit_repair, name='edit_repair'),
    path('delete_repair/<int:pk>/', views.delete_repair, name='delete_repair'),
    path('repairs/', views.repair_list, name='repair_list'),
]