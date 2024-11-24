from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bms_user_authentication.urls')),
    path('buses/', include('bms_bus_information_management.urls')),
    path('employees/', include('bms_driversworkers_management.urls')),
    path('schedules/', include('bms_bus_schedule_management.urls')),
    path('maintenance/', include('bms_maintenancerepair_management.urls')),
    path('dashboard/', include('bms_dashboard.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)