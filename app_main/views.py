from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from django.views import View
from .models import Invitation
import json

def index(request):
    invitations = Invitation.objects.all().order_by('-id')

    context = {
        'invitations' : invitations,
    }

    return render(request, 'index.html', context=context)


class CreateInvitationView(View):
    def get(self, request):
        return render(request, 'create.html')

    def post(self, request):
        response = {}
        
        body = request.body.decode('utf8')
        data = json.loads(body)

        invitation = Invitation()

        invitation.invi_title = data['invi_title']
        invitation.invi_writer = data['invi_writer']
        invitation.invi_input_date = timezone.datetime.now()
        invitation.invi_content = data['invi_content']

        invitation.save()

        response["result"] = "true"
        response["status_code"] = "200"
        response["message"] = "성공!"
        response["return_url"] = "/"

        return JsonResponse(response, json_dumps_params = {'ensure_ascii': False})