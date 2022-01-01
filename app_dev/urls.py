from django.urls import path
from . import views

# local dev test
urlpatterns = [
    path('', views.index, name="index"),
    path('test_json/', views.test_json, name="test_json"),
    path('singup/', views.CreateUserView.as_view(), name='singup'),
    path('main/', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
