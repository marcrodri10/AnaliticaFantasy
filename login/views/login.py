from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import View, TemplateView
import requests


class LoginView(View):
    template_name = "login/login.html"

    def get(self, request):
        
        return render(request, self.template_name)
    
    def post(self, request):
        token = request.POST.get("token")
        response = HttpResponse("Cookie establecida")
        response.set_cookie('token', token, max_age=3600)

        return redirect(request.GET.get('next', '/'))