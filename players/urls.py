from django.urls import path
from .views import players, player

urlpatterns = [
    path('players/', players.PlayersView.as_view(), name="players"),
    path('players/api/', players.PlayersViewApi.as_view(), name="players-api"),
    path('players/get/', players.Players.as_view(), name="players-get"),
    path('players/<int:id>', player.PlayerView.as_view(), name="player")
]