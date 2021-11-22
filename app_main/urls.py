from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index_test', views.index_test, name="index_test"),
]
