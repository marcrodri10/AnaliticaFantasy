from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views.generic import View, TemplateView, ListView
import requests


class PlayersView(View):
    template_name = "players/players.html"

    def get(self, request):
        players = requests.get("https://api.laligafantasymarca.com/api/v3/players")
        
        if players.status_code == 200:
             return render(request, self.template_name, {"players":players.json()})
        else:
            print(players.status_code, players.text)
       