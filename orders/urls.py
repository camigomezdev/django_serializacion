"""
URL configuration for the orders app.
"""

from django.urls import path
from .views import OrderAPIView
from rest_framework import status

urlpatterns = [
    path('orders/', OrderAPIView.as_view(), name='order-view'),
]
