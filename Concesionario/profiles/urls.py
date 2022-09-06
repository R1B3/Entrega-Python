from django.urls import path
from django.contrib.auth.models import User
from profiles.views import *
from proyecto.views import *


urlpatterns = [
    
    #Perfil
    path("",profile_view.as_view(),name = "profile"),
    
    #SignUp
    path('signup/',create_profile.as_view(),name = "signup"),
    
    #Update
    path("profile/<int:pk>",profile_view.as_view(),name = "update_profile"),
    
    #Edit
    path("edit_profile/<int:pk>/",edit_profile.as_view(),name = "edit_profile"),
   
] 