
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from bms_bus_information_management.models import Bus
from bms_bus_schedule_management.forms import ScheduleForm
from bms_bus_schedule_management.models import Schedule
from django.core.paginator import Paginator
from bms_bus_information_management.models import Bus
from bms_bus_schedule_management.models import Employee

from bms_driversworkers_management.models import Employee

# Create your views here.
@login_required
def add_schedule(request):
    buses = Bus.objects.filter(user=request.user)  # Fetch buses
    employees = Employee.objects.filter(user=request.user)  # Fetch employees filtered by user
    form = ScheduleForm()  # Initialize your form
    
    if request.method == "POST":
        form = ScheduleForm(request.POST)  # Pass user to the form
        if form.is_valid():
            form.save()  # Save the schedule with the selected bus
            return redirect('schedule_list')  # Redirect after saving
        else:
            print(form.errors)  # Debugging
    else:
        
        form = ScheduleForm()  # Initialize form without user context
    return render(request, 'bms_bus_schedule_management/home_page_schedule.html', {
        'form': form,
        'buses': buses,
        'employees': employees,
    })

@login_required
def edit_schedule(request, sched_id):
    schedule = get_object_or_404(Schedule, sched_id=sched_id)  # Fetch the schedule
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)  # Remove 'user' argument
        if form.is_valid():
            form.save()
            return redirect('schedule_list')  # Adjust to the home page or schedule list view
    else:
        form = ScheduleForm(instance=schedule)  # Remove 'user' argument
    return render(request, 'bms_bus_schedule_management/edit_schedule.html', {'form': form})

@login_required
def delete_schedule(request, sched_id):
    schedule = get_object_or_404(Schedule, sched_id=sched_id)  # Fetch the schedule
    if request.method == 'POST':
        schedule.delete()
        return redirect('schedule_list')  # Redirect after deletion
    return render(request, 'bms_bus_schedule_management/confirm_delete_schedule.html', {'object': schedule})

def schedule_list(request):
    schedules = Schedule.objects.filter(bus__user=request.user)  # Fetch schedules
    buses = Bus.objects.filter(user=request.user)  # Fetch buses
    employees = Employee.objects.filter(user=request.user)  # Fetch employees filtered by user
    form = ScheduleForm()  # Initialize your form

    return render(request, 'bms_bus_schedule_management/home_page_schedule.html', {
        'schedules': schedules,
        'buses': buses,
        'employees': employees,
        'form': form,
    })

def schedule_history(request, sched_id):
    schedule = get_object_or_404(Schedule, pk=sched_id)
    history = schedule.history.filter(bus__user=request.user).order_by('-updated_at')
    
    paginator = Paginator(history, 15)  # Show 15 history records per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'bms_bus_schedule_management/schedule_history.html', {
        'schedule': schedule,
        'page_obj': page_obj,
        'paginator': paginator
    })

def start_schedule(request, sched_id):
    schedule = get_object_or_404(Schedule, pk=sched_id)
    if schedule.departure_time is None and schedule.employee is not None:
        schedule.departure_time = timezone.now()
        schedule.status = 'in_transit'
        schedule.bus.status = 'in_transit'
        schedule.save()
        schedule.bus.save()
    return redirect('schedule_list')

def stop_schedule(request, sched_id):
    schedule = get_object_or_404(Schedule, pk=sched_id)
    if schedule.departure_time is not None and schedule.arrival_time is None:
        schedule.arrival_time = timezone.now()
        schedule.status = 'arrived'
        schedule.bus.status = 'On Standby'
        schedule.save()
        schedule.bus.save()
        schedule.departure_time = None
        schedule.arrival_time = None
        schedule.save()
    return redirect('schedule_list')

