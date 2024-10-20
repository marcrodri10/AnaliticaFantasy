from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views.generic import View, TemplateView
import requests


class LoginView(View):
    template_name = "login/login.html"

    def get(self, request):
        return render(request, self.template_name)
    
    """ def post(self, request):
        token = request.POST.get("token")

        players = requests.get("https://api.laligafantasymarca.com/api/v3/players")
        
        if players.status_code == 200:
            print(players.json())
        else:
            print(players.status_code, players.text)
        return render(request, "login/redirect.html", {"players":players.json()}) """