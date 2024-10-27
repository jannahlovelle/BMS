from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from bms_app.models import Bus, Employee, Schedule, UserProfile, Repair
from .forms import BusForm, EmployeeForm, LoginForm, RepairForm, ScheduleForm, UserPasswordChangeForm, UserProfileForm

# Views

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home_page')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def home_page(request):
    employees = Employee.objects.filter(user=request.user)
    buses = Bus.objects.filter(user=request.user)
    schedules = Schedule.objects.filter(bus__user=request.user)  # Filter schedules by the user of the related bus
    repairs = Repair.objects.filter(bus__user=request.user)  # Filter repairs by the user of the related bus
    return render(request, 'home_page.html', {
        'employees': employees,
        'buses': buses,
        'schedules': schedules,
        'repairs': repairs
    })


@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.user = request.user  # Associate with logged-in user
            employee.save()
            return redirect('home_page')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})


def user_list(request):
    users = User.objects.all()  # Fetch all users
    return render(request, 'user_list.html', {'users': users})


def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'confirm_delete.html', {'user': user})




@login_required
def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id, user=request.user)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {'form': form, 'employee': employee})


@login_required
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id, user=request.user)
    if request.method == 'POST':
        employee.delete()
        return redirect('home_page')
    return render(request, 'confirm_delete_employee.html', {'employee': employee})


@login_required
def add_bus(request):
    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            bus = form.save(commit=False)
            bus.user = request.user
            bus.save()
            return redirect('home_page')
    else:
        form = BusForm()
    return render(request, 'add_bus.html', {'form': form})


@login_required
def edit_bus(request, bus_id):
    bus = get_object_or_404(Bus, pk=bus_id, user=request.user)
    if request.method == 'POST':
        form = BusForm(request.POST, instance=bus)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = BusForm(instance=bus)
    return render(request, 'edit_bus.html', {'form': form})


@login_required
def delete_bus(request, bus_id):
    bus = get_object_or_404(Bus, pk=bus_id, user=request.user)
    if request.method == 'POST':
        bus.delete()
        return redirect('home_page')
    return render(request, 'confirm_delete_bus.html', {'bus': bus})


@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST' and 'update_profile' in request.POST:
        user_form = UserProfileForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile')
    else:
        user_form = UserProfileForm(instance=request.user)

    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile': user_profile
    })

@login_required
def change_password(request):
    if request.method == 'POST':
        password_form = UserPasswordChangeForm(request.user, request.POST)  # Use the custom form
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Important! Keep the user logged in
            return redirect('profile')  # Redirect to the profile page or wherever you want
    else:
        password_form = UserPasswordChangeForm(request.user)  # Initialize form for GET requests

    return render(request, 'change_password.html', {
        'password_form': password_form,
    })


@login_required
def add_schedule(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)  # Pass user to the form
        if form.is_valid():
            form.save()  # Save the schedule with the selected bus
            return redirect('schedule_list')  # Redirect after saving
    else:
        form = ScheduleForm()  # Initialize form without user context
    return render(request, 'add_schedule.html', {'form': form})

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
    return render(request, 'edit_schedule.html', {'form': form})

@login_required
def delete_schedule(request, sched_id):
    schedule = get_object_or_404(Schedule, sched_id=sched_id)  # Fetch the schedule
    if request.method == 'POST':
        schedule.delete()
        return redirect('schedule_list')  # Redirect after deletion
    return render(request, 'confirm_delete_schedule.html', {'object': schedule})

# Create a repair
def add_repair(request):
    if request.method == 'POST':
        form = RepairForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('repair_list')  # Replace with your redirect URL
    else:
        form = RepairForm()
    return render(request, 'add_repair.html', {'form': form})

# Edit a repair
def edit_repair(request, pk):
    repair = get_object_or_404(Repair, pk=pk)
    if request.method == 'POST':
        form = RepairForm(request.POST, instance=repair)
        if form.is_valid():
            form.save()
            return redirect('repair_list')  # Replace with your redirect URL
    else:
        form = RepairForm(instance=repair)
    return render(request, 'edit_repair.html', {'form': form})

# Delete a repair
def delete_repair(request, pk):
    repair = get_object_or_404(Repair, pk=pk)
    if request.method == 'POST':
        repair.delete()
        return redirect('repair_list')  # Replace with your redirect URL
    return render(request, 'delete_repair.html', {'repair': repair})

def bus_list(request):
    buses = Bus.objects.filter(user=request.user)
    return render(request, 'home_page.html', {'buses': buses})

def employee_list(request):
    employees = Employee.objects.filter(user=request.user)
    return render(request, 'home_page_employees.html', {'employees': employees})

def schedule_list(request):
    schedules = Schedule.objects.filter(bus__user=request.user)
    return render(request, 'home_page_schedule.html', {'schedules': schedules})

def repair_list(request):
    repairs = Repair.objects.filter(bus__user=request.user)
    return render(request, 'home_page_repair.html', {'repairs': repairs})