
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from bms_bus_schedule_management.forms import ScheduleForm
from bms_bus_schedule_management.models import Schedule
from django.core.paginator import Paginator

# Create your views here.
@login_required
def add_schedule(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)  # Pass user to the form
        if form.is_valid():
            form.save()  # Save the schedule with the selected bus
            return redirect('schedule_list')  # Redirect after saving
    else:
        form = ScheduleForm()  # Initialize form without user context
    return render(request, 'bms_bus_schedule_management/add_schedule.html', {'form': form})

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
    schedules = Schedule.objects.filter(bus__user=request.user)
    return render(request, 'bms_bus_schedule_management/home_page_schedule.html', {'schedules': schedules})

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

@login_required
def schedule_homepage(request):
    # employees = Employee.objects.filter(user=request.user)
    schedule = Schedule.objects.filter(user=request.user)
    # schedules = Schedule.objects.filter(bus__user=request.user)  # Filter schedules by the user of the related bus
    # repairs = Repair.objects.filter(bus__user=request.user)  # Filter repairs by the user of the related bus
    return render(request,  'bms_bus_information_management/home_page_schedule.html', {
        # 'employees': employees,
        'buses': schedule,
        # 'schedules': schedules,
        # 'repairs': repairs
    })

