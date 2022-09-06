from django import forms
from profiles.models import Profile
from django.contrib.auth.models import User
from proyecto.forms import User_registration_form

class Profile_form(User_registration_form):
    
    class Meta:
        model = Profile
        fields = "__all__" 