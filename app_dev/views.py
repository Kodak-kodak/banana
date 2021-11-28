from django.shortcuts import render

# local dev test
def index(request):
    return render(request, 'index.html')
