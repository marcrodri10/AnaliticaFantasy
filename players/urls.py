from django.urls import path
from .views import players, player

urlpatterns = [
    path('players/', players.PlayersView.as_view(), name="players"),
    path('players/<int:id>', player.PlayerView.as_view(), name="player")
]