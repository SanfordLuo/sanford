from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from apps.user.models import User
from common import utils


# /user/center
class UserView(View):
    def get(self, request):
        request = self.request.GET
        user_id = request.get('user_id')

        user_info = User.objects.get(id=user_id)

        data = {
            'user_id': user_info.id,
            'uuid': user_info.uuid,
            'username': user_info.username
        }
        return utils.json_response(is_succ=True, data=data)

    def post(self, request):
        request = self.request.POST

        username = request.get('username')
        avatar = request.get('avatar')
        password = request.get('password')
        phone = request.get('phone')
        email = request.get('email')
