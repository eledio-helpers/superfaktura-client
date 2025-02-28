"""
Data Format Enumeration.

This module provides an enumeration of data formats that can be used in the SuperFaktura API.

Classes:
    - DataFormat: Enumeration of data formats.

Usage:
    from superfaktura.enumerations.data_format import DataFormat
    data_format = DataFormat.JSON
"""

import enum


class DataFormat(enum.Enum):
    """
    Data Format Enumeration.

    This enumeration represents the different data formats that can be used in the SuperFaktura API.

    Values:
        - JSON: JSON format
        - PDF: PDF format

    Usage:
        data_format = DataFormat.JSON
    """

    JSON = enum.auto()
    PDF = enum.auto()
