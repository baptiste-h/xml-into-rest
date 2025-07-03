from datetime import datetime
from django.test import TestCase
from xml.etree.ElementTree import Element
from orders.utils import FormatType, format_xml_data


class FormatXmlDataTests(TestCase):
    def test_format_str(self):
        """Element is formatted as string without trailing spaces"""
        element = Element("test")
        element.text = " Order "
        result = format_xml_data(element, FormatType.STR)
        self.assertEqual(result, "Order")

    def test_format_int(self):
        """Element is formatted as int"""
        element = Element("test")
        element.text = "1 "
        result = format_xml_data(element, FormatType.INT)
        self.assertEqual(result, 1)

    def test_format_float(self):
        """Element is formatted as float"""
        element = Element("test")
        element.text = " 1.1"
        result = format_xml_data(element, FormatType.FLOAT)
        self.assertEqual(result, 1.1)

    def test_format_date(self):
        """Element is formatted as date"""
        element = Element("test")
        element.text = " 2025-07-03 "
        result = format_xml_data(element, FormatType.DATE)
        self.assertEqual(result, datetime(2025, 7, 3).date())

    def test_format_none(self):
        """Empty element results in None"""
        element = Element("test")
        element.text = None
        result = format_xml_data(element, FormatType.STR)
        self.assertEqual(result, None)

    def test_format_empy_string(self):
        """Element with empty string results in None"""
        element = Element("test")
        element.text = " "
        result = format_xml_data(element, FormatType.STR)
        self.assertEqual(result, None)

    def test_type_error(self):
        """Fails if wrong type argument"""
        element = Element("test")
        element.text = "test"
        with self.assertRaisesMessage(
            TypeError, "format_type must be an instance of Format Enum"
        ):
            format_xml_data(element, "")
