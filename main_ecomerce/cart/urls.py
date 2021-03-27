from django.urls import path
from . import views

urlpatterns = [
    path('addToCart', views.add_to_cart, name="addToCart")
]
