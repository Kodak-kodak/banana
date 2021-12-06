from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.models import User

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

class CreateUserView(View):

    print('start CreateUserView !!!')

    def get(self, request):
        data = {'method':'get'}
        
        return JsonResponse(data)

    def post(self, request):
        data = {'user_id':'test1', 'user_pw1':'test1', 'user_pw2':'test1'}

        if data['user_pw1'] == data['user_pw2']: # 비밀번호 1과 2를 비교해 같을 경우 다음 함수 실행
            user = User.objects.create_user(
                username = data['user_id'],
                password = data['user_pw1'],
            )

        return JsonResponse(data)
