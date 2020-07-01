from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Product, Order, Tag

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    context = {
        "user": request.user,
        "products": Product.objects.all(),
        'tag': Tag.objects.all(),
        'order': Order.objects.all(),
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
        if first_name is None:
            return render(request,"orders/register.html",{"message":"You must enter a name."})
        last_name=request.POST["last_name"]
        if last_name is None:
            return render(request,"orders/register.html",{"message":"You must enter a Last Name."})
        username=request.POST["username"]
        if username is None:
            return render(request,"orders/register.html",{"message":"You must enter a username."})
        email=request.POST["email"]
        if email is None:
            return render(request,"orders/register.html",{"message":"You must enter a email."})
        password=request.POST["password"]
        password2=request.POST["password2"]
        if password is None:
            return render(request,"orders/register.html",{"message":"You must enter a password."})
        if password2 is None:
            return render(request,"orders/register.html",{"message":"You must enter a password."})
        if not password==password2:
            return render(request,"orders/register.html",{"message":"Passwords don't match."})
        user=User.objects.create_user(username,email,password)
        user.first_name=first_name
        user.last_name=last_name
        user.save()
        return render(request,"orders/login.html", {"message": "Registered!"})
    return render(request, "orders/register.html")

@login_required
def add(request, product_id):

    #Filter products by id
    product, created = Product.objects.get_or_create(Product, pk=product_id)
    order, created = Order.objects.get_or_create(customer=request.user)
    order.product.add(product_id)
    return HttpResponseRedirect(reverse("home"))

@login_required
def cart(request):
    context = {
        "user": request.user,
        'orders': Order.objects.all(),
    }
    return render(request, 'orders/cart.html', context)

@login_required
def initiateorder(request):
    order, created = Order.objects.get_or_create(customer=request.user)
    order.status = 'Initiated'
    order.save()
    context = {
        'orders': Order.objects.all(),
    }
    return render(request, 'orders/orderstatus.html', context)

@login_required
def orderstatus(request):
    order, created = Order.objects.get_or_create(customer=request.user)
    context = {
        'orders': Order.objects.all(),
    }
    return render(request, 'orders/orderstatus.html', context)