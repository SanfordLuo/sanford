from django.shortcuts import render, HttpResponse
from django.views.generic import View


# Create your views here.

# /user/center
class UserView(View):
    def get(self, request):
        return HttpResponse(111)
