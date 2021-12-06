from django.shortcuts import render
from django.http import JsonResponse

# local dev test
def index(request):
    return render(request, 'index.html')

def test_json(request):
    if request.method == 'POST':    
        print('===================')
        print('POST')
        print(request.POST)
        print(request.POST.get)
        print('===================')
        data = {'email':'test_post@gmail.com'}
    elif request.method == 'GET':
        print('===================')
        print('GET')
        print('===================')
        data = {'email':'test_get@gmail.com'}
    return JsonResponse(data)
