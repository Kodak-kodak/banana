from django.contrib import admin
from django.urls import path, include
from app_main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('main/', include('app_main.urls')),
    path('member/', include('app_member.urls')),
    path('dev/', include('app_dev.urls')),
]
