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
             
        return render(request, self.template_name, {"data_paged": data_paged})
        

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