from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views.generic import View, TemplateView, ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.core.cache import cache
import json
import requests

POSITIONS = {
    1:"Portero",
    2:"Defensa",
    3: "Centrocampista",
    4: "Delantero",
    5: "Entrenador"
}
TEAMS = {
    2: "Atlético de Madrid",
    4: "FC Barcelona",
    3: "Athelic Club",
    5: "Real Betis",
    6: "RC Celta",
    8: "RCD Espanyol de Barcelona",
    9: "Getafe CF",
    13: "C.A. Osasuna",
    14: "Rayo Vallecano",
    15: "Real Madrid",
    16: "Real Sociedad",
    17: "Sevilla FC",
    18: "Valencia CF",
    19: "Real Valladolid CF",
    20: "Villareal CF",
    21: "Deportivo Alavés",
    28: "Girona FC",
    31: "UD Las Palmas",
    33: "RCD Mallorca",
    54: "CD Leganés"
}
class PlayersView(View):
    template_name = "players/players.html"

    def get(self, request):
        paginator = cache.get("players_paginator")
        
        if paginator is None:
            players = requests.get("https://api.laligafantasymarca.com/api/v3/players")
            cache.set("players_data", players.json(), 60*60)
            if players.status_code == 200:
                ##10pags
                paginator = Paginator(players.json(), 60)
                cache.set("players_paginator", paginator, 60*60)
            else:
                print(players.status_code, players.text)
        
            
        page = request.GET.get('page', 1)
        try:
            data_paged = paginator.page(page)
        except PageNotAnInteger:
            data_paged = paginator.page(1)
        except EmptyPage:
            data_paged = paginator.page(paginator.num_pages)
             
        return render(request, self.template_name, {"data_paged": data_paged, "positions": POSITIONS, "teams": TEAMS})
        

class PlayersViewApi(View):
    def get(self, request): 

        page = request.GET.get('page', 1)
        paginator = cache.get("players_paginator")
        try:
            data_paged = paginator.page(page)
        except PageNotAnInteger:
            data_paged = paginator.page(1)
        except EmptyPage:
            data_paged = paginator.page(paginator.num_pages)
            
        data = {
            "players": list(data_paged)
        }
        return JsonResponse(data)
    
class Players(View):
    def get(self, request): 

        players = cache.get("players_data")
        data = {
            "players": list(players)
        }
        return JsonResponse(data)