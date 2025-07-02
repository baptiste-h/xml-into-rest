from django.core.management.base import BaseCommand
import xml.etree.ElementTree as ET

from orders.utils import Format, format_xml_data
from orders.models import Order


class Command(BaseCommand):
    help = "Import xml file"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        file_path = options["file_path"]
        tree = ET.parse(file_path)
        root = tree.getroot()

        orders_data = []
        created_orders_count = 0

        # Retrieve data from XML in an array
        try:
            for order in root.iter("order"):
                order_dict = {
                    "order_id": format_xml_data(order.find("order_id")),
                    "marketplace": format_xml_data(order.find("marketplace")),
                    "order_status": format_xml_data(order.find("order_status/lengow")),
                    "order_purchase_date": format_xml_data(
                        order.find("order_purchase_date"), Format.DATE
                    ),
                    "order_amount": format_xml_data(
                        order.find("order_amount"), Format.FLOAT
                    ),
                    "order_shipping": format_xml_data(
                        order.find("order_shipping"), Format.FLOAT
                    ),
                }
                orders_data.append(order_dict)

        except Exception as e:
            self.stderr.write(
                self.style.ERROR(f"Error getting orders data from XML : {e}")
            )

        # Create orders if no problem occured during data retrieval
        try:
            for order_data in orders_data:
                Order.objects.create(
                    order_id=order_data["order_id"],
                    marketplace=order_data["marketplace"],
                    order_status=order_data["order_status"],
                    order_purchase_date=order_data["order_purchase_date"],
                    order_amount=order_data["order_amount"],
                    order_shipping=order_data["order_shipping"],
                )
                created_orders_count = created_orders_count + 1

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error creating order : {e}"))
            self.stderr.write(
                self.style.ERROR(f"{created_orders_count} have been created.")
            )

        self.stdout.write(
            self.style.SUCCESS(f"{created_orders_count} orders imported successfully.")
        )
