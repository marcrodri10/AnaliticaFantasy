from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views.generic import View, TemplateView, ListView
from django.core.paginator import Paginator
from django.http import JsonResponse
import json
import requests


class PlayersView(View):
    template_name = "players/players.html"

    def get(self, request):
        players = requests.get("https://api.laligafantasymarca.com/api/v3/players")
        
        if players.status_code == 200:
            paginator = Paginator(players.json(), 71)

            page = request.GET.get('page', 1)
            try:
                data_paged = paginator.page(page)
            except PageNotAnInteger:
                data_paged = paginator.page(1)
            except EmptyPage:
                data_paged = paginator.page(paginator.num_pages)
             
            return render(request, self.template_name, {"data_paged": data_paged})
        else:
            print(players.status_code, players.text)
       