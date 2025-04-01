
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name="checkout"),
    path('checkout_success/<order_number>', views.checkout_sucess, name='checkout_success'),
]
