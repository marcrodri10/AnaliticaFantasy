from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views.generic import View, TemplateView, ListView
from django.http import HttpResponse
import requests


class PlayerView(View):
    template_name = "players/player.html"
    PLAYER_URL = 'https://api.laligafantasymarca.com/api/v3/player/'
    
    def get(self, request, id):
        """ if(request.COOKIES.get("token") is None):
            return redirect(f"/login/?next={self.PLAYER_URL}{id}") """
        
        players = requests.get(f"{self.PLAYER_URL}{id}")
            
        if players.status_code == 200:
            return render(request, self.template_name, {"player":players.json()})
        else:
            print(players.status_code, players.text)
       