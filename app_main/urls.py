from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),


    # local dev test
    path('dev_index', views.dev_index, name="dev_index"),
]
