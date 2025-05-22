"""
Serializers for the Order app.
"""

from rest_framework import serializers
from .models import Product, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock', 'active']


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

    # Descomenta esto si quieres evitar que se haga una compra si no hay suficinete stock
    # def validate(self, data):
    #     product = data["product"]
    #     quantity = data["quantity"]

    #     if product.stock < quantity:
    #         raise serializers.ValidationError("No hay suficiente stock")

    #     return data

    def to_representation(self, instance):
        data = super().to_representation(instance)

        product = instance.product
        quantity = instance.quantity
        data['producto'] = product.name
        data['precio_unitario'] = float(product.price)
        data['subtotal'] = float(product.price * quantity)
        data['estado'] = "Disponible" if product.stock > 0 else "Agotado"

        # Mostrar nota si se recortó la cantidad
        original_quantities = self.context.get('original_quantities', {})
        original_requested = original_quantities.get(product.id)

        if original_requested and original_requested > quantity:
            data['nota'] = (
                f"Solicitaste {original_requested}, pero solo se agregaron {quantity} por disponibilidad de stock."
            )

        return data


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'created_at', 'items']

    def validate_customer(self, customer):
        if not customer.is_active:
            raise serializers.ValidationError("El cliente está inactivo.")
        return customer

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        # Guardamos la cantidad originalmente solicitada para usar en la respuesta
        original_quantities = {}

        for item_data in items_data:
            product = item_data['product']
            requested_quantity = item_data['quantity']
            available_quantity = min(requested_quantity, product.stock)

            # Guardar cantidad original para después mostrarla
            original_quantities[product.id] = requested_quantity

            # Crear el OrderItem con la cantidad ajustada
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=available_quantity
            )

            # Actualizar stock del producto
            product.stock -= available_quantity
            product.save()

        # Guardar contexto para usar luego en la representación
        self.context['original_quantities'] = original_quantities
        return order

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data["created_at"] = instance.created_at.strftime("%d/%m/%Y")

        total = sum([
            item.product.price * item.quantity
            for item in instance.items.select_related('product')
        ])

        data["total"] = total

        return data
