"""Views for the orders app."""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer
from rest_framework import status
from .models import Order


class OrderAPIView(APIView):
    """API view for orders."""

    def get(self, request):
        orders = Order.objects.all().select_related(
            'customer').prefetch_related('items__product')

        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """Handle POST requests."""
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileAPIView(APIView):
    """API view for user profile."""

    def get(self, request):
        """Handle GET requests."""

        return Response({
            'username': request.user.username,
            'email': request.user.email,
            'exp': request.auth["exp"],
            'user_id': request.auth["user_id"]
        })
