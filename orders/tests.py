from django.test import TestCase
from .models import Product, Order


class OrderModelTests(TestCase):
    def test_order_creation(self):
        product = Product.objects.create(name='Bread', time_to_cook=30)
        order = Order.objects.create(person_name='John', quantity=2, product=product)
        self.assertEqual(order.product.name, 'Bread')
        self.assertEqual(order.quantity, 2)