import os
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from bms_driversworkers_management.forms import DriverScheduleForm, EmployeeForm
from bms_driversworkers_management.models import DriverSchedule, Employee

# Create your views here.
@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.user = request.user  # Associate with logged-in user
            employee.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'bms_driversworkers_management/add_employee.html', {'form': form})


@login_required
def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id, user=request.user)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            # Check if a new photo is uploaded
            if 'photo' in request.FILES:
                # If the employee has an existing photo, delete it
                if employee.photo and os.path.isfile(employee.photo.path):
                    os.remove(employee.photo.path)

            # Save the updated employee data (including the new photo)
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'bms_driversworkers_management/edit_employee.html', {'form': form, 'employee': employee})


@login_required
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id, user=request.user)
    if employee.photo and os.path.isfile(employee.photo.path):
        os.remove(employee.photo.path)
    
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'bms_driversworkers_management/confirm_delete_employee.html', {'employee': employee})

def employee_list(request):
    employees = Employee.objects.filter(user=request.user)
    return render(request, 'bms_driversworkers_management/home_page_employees.html', {'employees': employees})

# DRIVERSCHEDULE
@login_required
def add_driver_schedule(request):
    if request.method == 'POST':
        form = DriverScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('driver_schedule_list')
    else:
        form = DriverScheduleForm()
    return render(request, 'bms_driversworkers_management/add_driver_schedule.html', {'form': form})

# List all DriverSchedules
@login_required
def driver_schedule_list(request):
    schedules = DriverSchedule.objects.all()
    return render(request, 'bms_driversworkers_management/driver_schedule_list.html', {'schedules': schedules})

# Edit an existing DriverSchedule
@login_required
def edit_driver_schedule(request, pk):  # Use 'id' as the parameter
    schedule = get_object_or_404(DriverSchedule, pk=pk)
    if request.method == 'POST':
        form = DriverScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('driver_schedule_list')
    else:
        form = DriverScheduleForm(instance=schedule)
    return render(request, 'bms_driversworkers_management/edit_driver_schedule.html', {'form': form})

# Delete a DriverSchedule
@login_required
def delete_driver_schedule(request, pk):  # Use 'id' as the parameter
    schedule = get_object_or_404(DriverSchedule, pk=pk)
    if request.method == 'POST':
        schedule.delete()
        return redirect('driver_schedule_list')
    return render(request, 'confirm_delete_driver_schedule.html', {'schedule': schedule})