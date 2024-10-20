from django.urls import path
from .views import players

urlpatterns = [
    path('', players.PlayersView.as_view(), name="players"),
]