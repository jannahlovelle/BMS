from django.shortcuts import get_object_or_404, redirect, render

from bms_maintenancerepair_management.forms import RepairForm
from bms_maintenancerepair_management.models import Repair

# Create your views here.
def add_repair(request):
    if request.method == 'POST':
        form = RepairForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('repair_list')  # Replace with your redirect URL
    else:
        form = RepairForm()
    return render(request, 'bms_maintenancerepair_management/add_repair.html', {'form': form})

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
    return render(request, 'bms_maintenancerepair_management/edit_repair.html', {'form': form})

# Delete a repair
def delete_repair(request, pk):
    repair = get_object_or_404(Repair, pk=pk)
    if request.method == 'POST':
        repair.delete()
        return redirect('repair_list')  # Replace with your redirect URL
    return render(request, 'bms_maintenancerepair_management/delete_repair.html', {'repair': repair})

def repair_list(request):
    repairs = Repair.objects.filter(bus__user=request.user)
    return render(request, 'bms_maintenancerepair_management/home_page_repair.html', {'repairs': repairs})