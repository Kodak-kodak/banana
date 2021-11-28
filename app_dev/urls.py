from django.urls import path
from . import views

# local dev test
urlpatterns = [
    path('', views.index, name="index"),
]
