from django.urls import path
from . import views

app_name = 'member'

urlpatterns = [
    path('singup/', views.CreateUserView.as_view(), name='singup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
