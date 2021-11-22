from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    data = {'email':'hansolove@gmail.com'}
    return JsonResponse(data)

def index_test(request):
    data = {'email':'hansolove@gmail.com', 'age':'20'}
    return JsonResponse(data)
