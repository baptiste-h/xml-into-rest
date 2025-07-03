from datetime import datetime
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from orders.models import Order


class OrderTests(TestCase):
    def setUp(self):
        """
        Create test orders
        """
        self.client = APIClient()
        self.orders = [
            {
                "id": "1",
                "order_id": "123",
                "order_purchase_date": datetime(2025, 7, 3).date(),
                "order_amount": 99.99,
                "order_shipping": 5.00,
                "order_status": "new",
                "marketplace": "amazon",
            },
            {
                "id": "2",
                "order_id": "124",
                "order_purchase_date": datetime(2024, 7, 3).date(),
                "order_amount": 199.99,
                "order_shipping": 2.50,
                "order_status": "cancel",
                "marketplace": "cdiscount",
            },
        ]
        for order in self.orders:
            Order.objects.create(**order)

    def test_get_orders(self):
        """
        All orders are listed
        """
        response = self.client.get("/api/order/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_order_detail(self):
        """
        Specific order can be retrieved
        """
        response = self.client.get("/api/order/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["order_id"], "123")

    def test_order_not_found(self):
        """
        Can't get unexisting order
        """
        response = self.client.get("/api/order/3/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
