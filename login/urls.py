from django.urls import path
from .views import login

urlpatterns = [
    path('', login.LoginView.as_view(), name="login"),
]