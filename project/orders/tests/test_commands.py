import os
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, ElementTree
from django.core.management import call_command
from django.test import TestCase

from orders.models import Order


class ImportXmlTests(TestCase):
    def setUp(self):
        """
        Create a temporary XML test file
        """
        self.xml_file_path = "test_orders.xml"
        self.create_test_xml_file()

    def tearDown(self):
        """
        Destroys XML test file after tests run
        """
        if os.path.exists(self.xml_file_path):
            os.remove(self.xml_file_path)

    def create_test_xml_file(self):
        """
        Create a test XML file
        """
        root = Element("root")
        orders = SubElement(root, "orders")
        order = SubElement(orders, "order")
        SubElement(order, "order_id").text = "123"
        SubElement(order, "marketplace").text = "amazon"
        SubElement(order, "order_purchase_date").text = "2025-07-03"
        SubElement(order, "order_amount").text = "99.99"
        SubElement(order, "order_shipping").text = "5.00"

        # order_status comes from "lengow" sub element
        order_status = SubElement(order, "order_status")
        SubElement(order_status, "lengow").text = "new"

        tree = ElementTree(root)
        tree.write(self.xml_file_path)

    def test_import_orders_success(self):
        """
        Execute import and check if order has been created in db
        """
        call_command("import_xml", self.xml_file_path)
        order = Order.objects.get(order_id="123")
        self.assertEqual(order.marketplace, "amazon")
        self.assertEqual(order.order_status, "new")
        self.assertEqual(order.order_purchase_date, datetime(2025, 7, 3).date())
        self.assertEqual(order.order_amount, 99.99)
        self.assertEqual(order.order_shipping, 5.00)
