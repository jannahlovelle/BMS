from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),  # Set the login page as the landing page
    path('home/', views.home_page, name='home_page'),
    path('logout/', views.user_logout, name='logout'),

    path('user_list/', views.user_list, name='user_list'),
    path('profile/', views.profile, name='profile'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('password/', views.change_password, name='change_password'),

    path('add_employee/', views.add_employee, name='add_employee'),
    path('employees/edit/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('employees/delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),

    path('buses/add/', views.add_bus, name='add_bus'),
    path('buses/edit/<int:bus_id>/', views.edit_bus, name='edit_bus'),
    path('buses/delete/<int:bus_id>/', views.delete_bus, name='delete_bus'),

    path('add_schedule/', views.add_schedule, name='add_schedule'),
    path('edit_schedule/<int:sched_id>/', views.edit_schedule, name='edit_schedule'),
    path('delete_schedule/<int:sched_id>/', views.delete_schedule, name='delete_schedule'),

    path('add_repair/', views.add_repair, name='add_repair'),
    path('edit_repair/<int:pk>/', views.edit_repair, name='edit_repair'),
    path('delete_repair/<int:pk>/', views.delete_repair, name='delete_repair'),

    path('buses/', views.bus_list, name='bus_list'),  # Optional: Separate bus list view
    path('employees/', views.employee_list, name='employee_list'),  # Optional: Separate employee list view
    path('schedules/', views.schedule_list, name='schedule_list'),  # Optional: Separate schedule list view
    path('repairs/', views.repair_list, name='repair_list'),  # Optional: Separate repair list view
    
    path('driver_schedule/add/', views.add_driver_schedule, name='add_driver_schedule'),
    path('driver_schedule/', views.driver_schedule_list, name='driver_schedule_list'),
    path('driver_schedule/edit/<int:pk>/', views.edit_driver_schedule, name='edit_driver_schedule'),
    path('driver_schedule/delete/<int:pk>/', views.delete_driver_schedule, name='delete_driver_schedule'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
