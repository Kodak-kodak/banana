from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('app_main.urls')),
    path('member/', include('app_member.urls')),
    path('dev/', include('app_dev.urls')),
]
