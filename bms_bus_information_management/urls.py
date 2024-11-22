
from django.urls import path
from bms_bus_information_management import views


urlpatterns=[
    path('buses/add/', views.add_bus, name='add_bus'),
    path('buses/edit/<int:bus_id>/', views.edit_bus, name='edit_bus'),
    path('buses/delete/<int:bus_id>/', views.delete_bus, name='delete_bus'),
    path('buses/', views.bus_list, name='bus_list'),  # Optional: Separate bus list view
    # path('home/', views.home_page, name='home_page')
]