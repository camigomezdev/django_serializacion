"""
URL configuration for the orders app.
"""

from django.urls import path
from .views import OrderAPIView, ProfileAPIView, OrderDetailView


urlpatterns = [
    path('orders/', OrderAPIView.as_view(), name='order-view'),
    path('orders/<int:pk>', OrderDetailView.as_view(), name='order-detail'),
    path('profile/', ProfileAPIView.as_view(), name='profile-view'),
]
