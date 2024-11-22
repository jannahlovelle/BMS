from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from bms_bus_information_management.models import Bus
from bms_user_authentication.forms import LoginForm, UserPasswordChangeForm, UserProfileForm
from bms_user_authentication.models import UserProfile

# Create your views here.

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
def user_homepage(request):
    # employees = Employee.objects.filter(user=request.user)
    buses = Bus.objects.filter(user=request.user)
    # schedules = Schedule.objects.filter(bus__user=request.user)  # Filter schedules by the user of the related bus
    # repairs = Repair.objects.filter(bus__user=request.user)  # Filter repairs by the user of the related bus
    return render(request,  'bms_bus_information_management/home_page.html', {
        # 'employees': employees,
        'buses': buses,
        # 'schedules': schedules,
        # 'repairs': repairs
    })