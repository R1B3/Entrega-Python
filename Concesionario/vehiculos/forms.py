from django import forms
from vehiculos.models import Cars, Motorcycles, Trucks

class Car_form(forms.ModelForm):
    class Meta:
        model = Cars
        fields = "__all__" 
class Truck_form(forms.ModelForm):
    class Meta:
        model = Trucks
        fields = "__all__"
class Motorcycle_form(forms.ModelForm):
    class Meta:
        model = Motorcycles
        fields = "__all__"
    