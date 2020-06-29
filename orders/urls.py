from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    url(r'^order/add/(?P<product_id>[-\w]+)/$', views.add, name="add"),
    path('cart', views.cart, name='cart' ),
]
