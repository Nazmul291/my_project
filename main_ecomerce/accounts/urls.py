from django.urls import path
from . import views

urlpatterns = [
    path('user/register', views.account_register, name="account_register"),
    path('user/login', views.account_login, name="account_login"),
    path('user/logout', views.account_logout, name="account_logout"),

]
