from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import pizza, topping, sub, pasta, salad, DinnerPlatter

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    context = {
        "user": request.user,
        "pizzas": pizza.objects.all(),
        "toppings": topping.objects.all(),
        "subs": sub.objects.all(),
        "pastas": pasta.objects.all(),
        "salads": salad.objects.all(),
        "DinnerPlatters": DinnerPlatter.objects.all()
    }
    return render(request, "orders/home.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out"})

def register(request):
    if request.method == 'POST':
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        password2=request.POST["password2"]
        if not password==password2:
            return render(request,"orders/register.html",{"message":"Passwords don't match."})
        user=User.objects.create_user(username,email,password)
        user.first_name=first_name
        user.last_name=last_name
        user.save()
        return render(request,"orders/login.html", {"message": "Registered!"})
    return render(request, "orders/register.html")