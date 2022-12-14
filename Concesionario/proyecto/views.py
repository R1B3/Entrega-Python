
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from proyecto.forms import User_registration_form




def index(request):
    print(request.user)
    print(request.user.is_authenticated)
    return render(request,'index.html')

def about_us(request):
    print(request.user)
    return render(request,'about_us.html')

def login_view(request):
    
        # entra por POST, formulario completado
        if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)
            
            #valida que el formulario esté correcto
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(username = username, password = password)
                
                if user is not None:
                    login(request,user)
                    context = {"message": f"Welcome {username}"}
                    return render(request, "index.html", context = context)
                else: 
                    context = {"error": "User don't exists. Try Again"}
                    form = AuthenticationForm()
                    return render(request, "auth/login.html", context = context)
            else:
                errors = form.errors
                print(errors)
                form = AuthenticationForm()
                context = {"errors": errors, "form": form}
                return render(request, "auth/login.html", context = context)
        
        # entra por GET, muestra el formulario en pantalla
        else:
            form = AuthenticationForm()
            context = {"form": form}
            return render(request, "auth/login.html", context = context)

def logout_view(request):
    logout(request)
    return redirect("index")

def signup_view(request):
    if request.method == "POST":
        form = User_registration_form(request.POST)
        
        if form.is_valid():
            form.save() 
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username = username, password = password)
            login(request,user)
            context = {"message":f"Usario creado correctamente, bienvenido {username}"}
            return render(request, "index.html", context = context)
        else:
            errors = form.errors
            form = User_registration_form()
            context = {"errors": errors, "form": form}
            return render(request, "auth/signup.html", context = context) 
    else:
        form = User_registration_form()
        context = {"form": form}
        return render(request, "auth/signup.html", context = context)
        