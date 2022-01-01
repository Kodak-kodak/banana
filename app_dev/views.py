from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.models import User
import json

from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings

# local dev test
def index(request):
    return render(request, 'index.html')

# local dev test
def main(request):
    return render(request, 'test_main.html')

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
    def get(self, request):
        data = {'method':'get'}
        return JsonResponse(data)

    def post(self, request):
        response = {}
        
        body = request.body.decode('utf8')
        data = json.loads(body)

        # testdata = {'userid':'test2', 'password1':'test1', 'password1':'test1'}

        if User.objects.filter(username=data['userid']): 
            response["result"] = "false"
            response["status_code"] = "500"
            response["message"] = "이미 사용중인 아이디 입니다."
            response["return_url"] = "/"
            return JsonResponse(response, json_dumps_params = {'ensure_ascii': False}) # Line 69과 중복이 되는데 맞는걸까
        else:
            if data['password1'] == data['password2']: # 비밀번호 1과 2 비교
                try:
                    user = User.objects.create_user(
                        username = data['userid'],
                        password = data['password1'],
                    )
                    auth.login(request, user)
                    return redirect('main')
                except KeyError:
                    response["result"] = "false"
                    response["status_code"] = "200"
                    response["message"] = "회원가입에 실패하였습니다."
                    response["return_url"] = "/"
            else :
                response["result"] = "false"
                response["status_code"] = "200"
                response["message"] = "비밀번호가 서로 다릅니다."
                response["return_url"] = "/"
            return JsonResponse(response, json_dumps_params = {'ensure_ascii': False})

class Loginviews(LoginView):
    template_name = 'login.html'
login = Loginviews.as_view()

class LogoutViews(LogoutView):
    next_page = settings.LOGOUT_REDIRECT_URL
logout = LogoutViews.as_view()
