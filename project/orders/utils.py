from datetime import datetime
from enum import Enum
from xml.etree.ElementTree import Element


class FormatType(Enum):
    """
    Types available to format_xml_data function.

    STR | INT | FLOAT | DATE
    """

    STR = "str"
    INT = "int"
    FLOAT = "float"
    DATE = "date"


def format_xml_data(element: Element | None, format_type=FormatType.STR):
    """
    Format xml data to desired format_type.

    If None, returns None without trying to format.
    """

    # Raise error if wrong format_type argument
    if not isinstance(format_type, FormatType):
        raise TypeError("format_type must be an instance of Format Enum")

    if element == None or element.text == None:
        return None

    # Remove trailing spaces
    formatted_data = element.text.strip()

    # Empty string turns into None
    if formatted_data == "":
        return None

    match format_type:
        case FormatType.STR:
            return formatted_data
        case FormatType.INT:
            return int(formatted_data)
        case FormatType.FLOAT:
            return float(formatted_data)
        case FormatType.DATE:
            return datetime.strptime(formatted_data, "%Y-%m-%d").date()
        case _:
            raise TypeError("format_type isinstance check error")
