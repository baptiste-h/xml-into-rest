from datetime import datetime
from enum import Enum
from xml.etree.ElementTree import Element


class Format(Enum):
    STR = "str"
    INT = "int"
    FLOAT = "float"
    DATE = "date"


def format_xml_data(element: Element | None, format=Format.STR):
    """
    Format xml data to desired format.
    If None, returns None without trying to format.
    """
    if not isinstance(format, Format):
        raise TypeError("format must be an instance of Format Enum")

    if element == None or element.text == None:
        return None

    formatted_data = element.text.strip()

    match format:
        case Format.INT:
            formatted_data = int(formatted_data)
        case Format.FLOAT:
            formatted_data = float(formatted_data)
        case Format.DATE:
            formatted_data = datetime.strptime(formatted_data, "%Y-%m-%d").date()

    return formatted_data
