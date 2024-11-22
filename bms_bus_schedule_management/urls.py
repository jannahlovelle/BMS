
from django.urls import path
from bms_bus_schedule_management import views

urlpatterns=[
    path('add_schedule/', views.add_schedule, name='add_schedule'),
    path('edit_schedule/<int:sched_id>/', views.edit_schedule, name='edit_schedule'),
    path('delete_schedule/<int:sched_id>/', views.delete_schedule, name='delete_schedule'),
    path('schedules/', views.schedule_list, name='schedule_list'),
]