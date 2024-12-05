from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from bms_bus_information_management.models import Bus
from bms_bus_schedule_management.models import ScheduleHistory
from bms_driversworkers_management.models import Employee
from django.db.models import Count
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@login_required
def dashboard(request):
    
    user = request.user
    
    total_buses = Bus.objects.filter(user=user).count()
    total_employees = Employee.objects.filter(user=user).count()
    buses_in_operation = Bus.objects.filter(user=user, status='in_transit').count()
    buses_under_maintenance = Bus.objects.filter(user=user, status='under_maintenance').count()
    
    recent_activities = [
        "Bus {} added".format(bus.plate_number) for bus in Bus.objects.filter(user=user).order_by('bus_id')[:5]
    ]
    notifications = [
        "Maintenance due for Bus {}".format(bus.plate_number) for bus in Bus.objects.filter(user=user, status='Maintenance Due')
    ]
    
    context = {
        'total_buses': total_buses,
        'total_employees': total_employees,
        'buses_in_operation': buses_in_operation,
        'buses_under_maintenance': buses_under_maintenance,
        'recent_activities': recent_activities,
        'notifications': notifications,
    }
    
    return render(request, 'bms_dashboard/dashboard.html', context)

@login_required
@csrf_exempt
def get_bus_data(request):
    user = request.user
    available_buses = Bus.objects.filter(user=user, status='on_standby').count()
    buses_in_operation = Bus.objects.filter(user=user, status='in_transit').count()
    buses_under_maintenance = Bus.objects.filter(user=user, status='under_maintenance').count()

    data = {
        'available_buses': available_buses,
        'buses_in_operation': buses_in_operation,
        'buses_under_maintenance': buses_under_maintenance,
    }
    return JsonResponse(data)


@login_required
@csrf_exempt
def get_employee_data(request):
    user = request.user
    total_employees = Employee.objects.filter(user=user).count()
    active_employees = Employee.objects.filter(user=user, status='active').count()
    inactive_employees = Employee.objects.filter(user=user, status='inactive').count()

    data = {
        'total_employees': total_employees,
        'active_employees': active_employees,
        'inactive_employees': inactive_employees,
    }
    return JsonResponse(data)

@login_required
@csrf_exempt
def get_bus_schedule_history(request):
    user = request.user
    schedule_history = ScheduleHistory.objects.filter(schedule__bus__user=user).values('schedule__route').annotate(count=Count('schedule_id')).order_by('schedule__route')

    data = {
        'schedule_history': list(schedule_history)
    }
    return JsonResponse(data)