from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

def index(request):
    data = {'email':'hansolove@gmail.com'}
    return JsonResponse(data)
