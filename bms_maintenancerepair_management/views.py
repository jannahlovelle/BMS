from django.shortcuts import get_object_or_404, redirect, render

from bms_maintenancerepair_management.forms import RepairForm
from bms_maintenancerepair_management.models import Repair
from bms_bus_information_management.models import Bus
from bms_driversworkers_management.models import Employee

# Create your views here.
def add_repair(request):

    if request.method == 'POST':
        form = RepairForm(request.POST, user=request.user)
        if form.is_valid():
            repair = form.save(commit=False)
            repair.status ='under_maintenance'
            repair.save()

            bus = repair.bus
            bus.status = 'under_maintenance'
            bus.save()

            return redirect('repair_list')  # Replace with your redirect URL
        else:
            print(form.errors)  # Debugging
    else:
        form = RepairForm(user=request.user)
        
    buses = Bus.objects.filter(user=request.user)  # Fetch buses
    employees = Employee.objects.filter(user=request.user)

    return render(request, 'bms_maintenancerepair_management/home_page_repair.html', {
        'form': form,
        'buses': buses,
        'employees': employees,
    })

# Edit a repair
def edit_repair(request, pk):
    repair = get_object_or_404(Repair, pk=pk)
    if request.method == 'POST':
        form = RepairForm(request.POST, instance=repair)
        if form.is_valid():
            repair = form.save()
            # Check if the repair status is "done" and update the bus status
            if repair.status == 'done':
                bus = repair.bus
                bus.status = 'On Standby'
                bus.save()
            return redirect('repair_list')  # Replace with your redirect URL
    else:
        form = RepairForm(instance=repair)
    return render(request, 'bms_maintenancerepair_management/edit_repair.html', {'form': form})

# Delete a repair
def delete_repair(request, pk):
    repair = get_object_or_404(Repair, pk=pk)
    if request.method == 'POST':
        repair.delete()
        return redirect('repair_list')  # Replace with your redirect URL
    return render(request, 'bms_maintenancerepair_management/delete_repair.html', {'repair': repair})

def repair_list(request):
    repairs = Repair.objects.all()
    buses = Bus.objects.filter(user=request.user)  # Fetch buses
    employees = Employee.objects.filter(user=request.user, status='active', job_title='mechanic')  # Fetch active mechanics filtered by user
    form = RepairForm(user=request.user)

    return render(request, 'bms_maintenancerepair_management/home_page_repair.html', {
        'repairs': repairs,
        'buses': buses,
        'employees': employees,
        'form': form
    })