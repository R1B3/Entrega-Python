from multiprocessing import context
from django import template
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import UpdateView,ListView,CreateView
from profiles.models import Profile 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.

class profile_view(ListView):
    model = Profile
    template_name = "profile.html"
    queryset: Profile.objects.filter



class edit_profile(LoginRequiredMixin,UpdateView):
    model = Profile
    template_name = "edit_profile.html"
    fields = "__all__"
    
    def get_success_url(self):
        return reverse("update_profile", kwargs= {"pk": self.object.pk})  



class create_profile(CreateView):
    model = Profile
    template_name = "auth/signup.html"
    fields = ["first_name", "last_name", "phone","adress", "city","gender","email",]

    def get_success_url(self):
        return reverse("profile", kwargs={"pk": self.object.pk})


#En el código debería estar el avatar creado, pero como no me dejó de tirar error decidí rendirme con eso... :(




