"""
URL configuration for the orders app.
"""

from django.urls import path
from .views import OrderAPIView, ProfileAPIView


urlpatterns = [
    path('orders/', OrderAPIView.as_view(), name='order-view'),
    path('profile/', ProfileAPIView.as_view(), name='profile-view'),
]
