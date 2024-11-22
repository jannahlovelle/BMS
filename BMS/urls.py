from django.contrib import admin
from django.urls import include, path

from django.conf.urls.static import static

from BMS import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('bms/', include('bms_app.urls')),
    path('', include('bms_user_authentication.urls')),
    path('buses/', include('bms_bus_information_management.urls')),
    path('employees/', include('bms_driversworkers_management.urls')),
    path('schedules/', include('bms_bus_schedule_management.urls')),
    path('maintenance/', include('bms_maintenancerepair_management.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)