from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import UpdateView, CreateView, DeleteView, DetailView, ListView
from vehiculos.models import Cars,Motorcycles,Trucks
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def buy(request):
    return render(request,'buy.html')

# ------- ELEMENT WITH CLASS--------

class list_car(ListView):
    model = Cars
    template_name = "list_car.html"
    queryset: Cars.objects.filter(is_active = True)

class list_motorcycle(ListView):
    model = Motorcycles
    template_name = "list_motorcycle.html"
    queryset: Motorcycles.objects.filter(is_active = True)

class list_truck(ListView):
    model = Trucks
    template_name = "list_truck.html"
    queryset: Trucks.objects.filter(is_active = True)



# -------- SEARCH ---------

def search_vehicle(request):
    print(request.GET)
    truck = Trucks.objects.filter(brand__icontains = request.GET["Search"])
    car = Cars.objects.filter(brand__icontains = request.GET["Search"])
    motorcycle = Motorcycles.objects.filter(brand__icontains = request.GET["Search"])
    context = {"cars": car, "trucks": truck, "motorcycles": motorcycle}
    return render(request,"search_vehicle.html", context = context)



# --------- CREATE ELEMENT WITH CLASS ----


class create_car_view(LoginRequiredMixin,CreateView):
    model = Cars
    template_name = "create_car.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse("car_details", kwargs={"pk": self.object.pk})



class create_motorcycle_view(LoginRequiredMixin,CreateView):
    model = Motorcycles
    template_name = "create_motorcycle.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse("motorcycle_details", kwargs={"pk": self.object.pk})



class create_truck_view(LoginRequiredMixin,CreateView):
    model = Trucks
    template_name = "create_truck.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse("truck_details", kwargs={"pk": self.object.pk})




# --------- DETAIL ELEMENT WITH CLASS ----


class detail_car_view(DetailView):
    model = Cars
    template_name = "details_car.html"
    fields = "__all__"

    
class detail_motorcycle_view(DetailView):
    model = Motorcycles
    template_name = "details_motorcycle.html"
    fields = "__all__"

    
class detail_truck_view(DetailView):
    model = Trucks
    template_name = "details_truck.html"
    fields = "__all__"
    
    
    
    
# ------- UPDATE ELEMENT WITH CLASS --------------


class update_car_view(LoginRequiredMixin,UpdateView):
    model = Cars
    template_name = "update_car.html"
    fields = "__all__"
    
    def get_success_url(self):
        return reverse("car_details", kwargs= {"pk": self.object.pk})



class update_motorcycle_view(LoginRequiredMixin,UpdateView):
    model = Motorcycles
    template_name = "update_motorcycle.html"
    fields = "__all__"
    
    def get_success_url(self):
        return reverse("motorcycle_details", kwargs= {"pk": self.object.pk})



class update_truck_view(LoginRequiredMixin,UpdateView):
    model = Trucks
    template_name = "update_truck.html"
    fields = "__all__"
    
    def get_success_url(self):
        return reverse("truck_details", kwargs= {"pk": self.object.pk})



# ------- DELETE ELEMENT WITH CLASS --------------

class delete_car_view(LoginRequiredMixin,DeleteView):
    model = Cars
    template_name = "delete_car.html"
    
    def get_success_url(self):
        return reverse("cars")


class delete_motorcycle_view(LoginRequiredMixin,DeleteView):
    model = Motorcycles
    template_name = "delete_motorcycle.html"
    
    def get_success_url(self):
        return reverse("motorcycles")
        
        
class delete_truck_view(LoginRequiredMixin,DeleteView):
    model = Trucks
    template_name = "delete_truck.html"
    
    def get_success_url(self):
        return reverse("trucks")