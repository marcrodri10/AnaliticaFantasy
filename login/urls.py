from django.urls import path
from .views import login

urlpatterns = [
    path('login/', login.LoginView.as_view(), name="login"),
]