from django.urls import path
from . import views

app_name = 'dev'

# local dev test
urlpatterns = [
    path('', views.index, name="index"),
]
