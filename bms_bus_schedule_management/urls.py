
from django.urls import path
from bms_bus_schedule_management import views

urlpatterns=[
    path('add_schedule/', views.add_schedule, name='add_schedule'),
    path('edit_schedule/<int:sched_id>/', views.edit_schedule, name='edit_schedule'),
    path('delete_schedule/<int:sched_id>/', views.delete_schedule, name='delete_schedule'),
    path('schedules/', views.schedule_list, name='schedule_list'),
    path('schedule/<int:sched_id>/history/', views.schedule_history, name='schedule_history'),
    path('schedule/<int:sched_id>/start/', views.start_schedule, name='start_schedule'),
    path('schedule/<int:sched_id>/stop/', views.stop_schedule, name='stop_schedule'),
    
    
]