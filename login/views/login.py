from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views.generic import View, TemplateView


class LoginView(TemplateView):
    template_name = "login/login.html"