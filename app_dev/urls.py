from django.urls import path
from . import views

# local dev test
urlpatterns = [
    path('', views.index, name="index"),
    path('test_json/', views.test_json, name="test_json"),
]
