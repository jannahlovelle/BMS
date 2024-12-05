from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from bms_bus_information_management.forms import BusForm
from bms_bus_information_management.models import Bus
from django.shortcuts import render
import logging
from django.contrib.auth.decorators import login_required
from bms_bus_information_management.models import Bus
from django.http import JsonResponse
from django.core.paginator import Paginator

logger = logging.getLogger(__name__)
# Create your views here.

@login_required
def add_bus(request):
    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            bus = form.save(commit=False)
            bus.user = request.user  # Set the user who is adding the bus
            bus.save()
            logger.info(f"Bus added successfully: {bus}")
            return redirect('home_page')
        else:
            logger.error(f"Form is invalid: {form.errors}")  # Log form errors
    else:
        form = BusForm()

    return render(request, 'bms_bus_information_management/home_page.html', {'form': form})


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
    paginator = Paginator(buses, 10)  # Show 10 buses per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'bms_bus_information_management/home_page.html', {'buses': buses})