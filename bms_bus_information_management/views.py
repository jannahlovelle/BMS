from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from bms_bus_information_management.forms import BusForm
from bms_bus_information_management.models import Bus

# Create your views here.

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
    return render(request, 'bms_bus_information_management/add_bus.html', {'form': form})


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
    return render(request, 'bms_bus_information_management/edit_bus.html', {'form': form})


@login_required
def delete_bus(request, bus_id):
    bus = get_object_or_404(Bus, pk=bus_id, user=request.user)
    if request.method == 'POST':
        bus.delete()
        return redirect('home_page')
    return render(request, 'bms_bus_information_management/confirm_delete_bus.html', {'bus': bus})

@login_required
def bus_list(request):
    buses = Bus.objects.filter(user=request.user)
    return render(request, 'bms_bus_information_management/home_page.html', {'buses': buses})