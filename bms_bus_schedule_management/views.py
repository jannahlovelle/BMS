from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from bms_bus_schedule_management.forms import ScheduleForm
from bms_bus_schedule_management.models import Schedule

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