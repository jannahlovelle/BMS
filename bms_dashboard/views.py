from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from bms_bus_information_management.models import Bus
from bms_driversworkers_management.models import Employee

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