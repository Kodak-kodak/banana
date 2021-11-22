from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    data = {'email':'hansolove@gmail.com'}
    return JsonResponse(data)
