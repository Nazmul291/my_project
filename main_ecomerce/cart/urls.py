from django.urls import path
from . import views

urlpatterns = [
    path('addToCart', views.addtocart, name="addToCart")
]
