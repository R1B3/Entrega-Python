
from django.urls import path
from vehiculos.views import *

urlpatterns = [
    
    #Comprar
    path('buy/',buy,name = "buy"),

    #Vehiculos
    path('cars/',list_car.as_view(),name = "cars"),
    path('motorcycles/',list_motorcycle.as_view(),name ="motorcycles"),
    path('trucks/',list_truck.as_view(),name ="trucks"),

    #Crear Vehiculo
    path('create-car/', create_car_view.as_view(),name="create_car"),
    path('create-truck/', create_truck_view.as_view(),name="create_truck"),
    path('create-motorcycle/',create_motorcycle_view.as_view(),name="create_motorcycle"),

    #Buscar
    path('search-vehicle/',search_vehicle,name="search_vehicle"),

    #Detalles Vehiculos
    path('car-details/<int:pk>/',detail_car_view.as_view(),name="car_details"),
    path('truck-details/<int:pk>/',detail_truck_view.as_view(),name="truck_details"),
    path('motorcycle-details/<int:pk>/',detail_motorcycle_view.as_view(),name="motorcycle_details"),

    #Eliminar Vehiculo
    path('delete-car/<int:pk>/',delete_car_view.as_view(),name="delete_car"),
    path('delete-motorcycle/<int:pk>/',delete_motorcycle_view.as_view(),name="detele_motorcycle"),
    path('delete-truck/<int:pk>/',delete_truck_view.as_view(),name="delete_truck"),

    #Actualizar/Editar
    path('update-car/<int:pk>/',update_car_view.as_view(),name="update_car"),
    path('update-motorcycle/<int:pk>/',update_motorcycle_view.as_view(),name="update_motorcycle"),
    path('update-truck/<int:pk>/',update_truck_view.as_view(),name="update_trucl"),

]

