"""
Data Types Module.

This module provides data types and utilities for working with dates and other data types
in the SuperFaktura API.

Classes:
    - Date: Represents a date in the format YYYY-MM-DD.
    - DateTime: Represents a date and time in the format YYYY-MM-DD HH:MM:SS.

Functions:
    - (none)

Usage:
    from superfaktura.utils.data_types import Date, DateTime
    date = Date("2022-01-01")
    datetime = DateTime("2022-01-01 12:00:00")
"""

from datetime import datetime
from typing import Optional

import json


class Date:
    """
    Date Class.

    This class represents a date in the format YYYY-MM-DD.

    Attributes:
        - date (str): The date in the format YYYY-MM-DD.

    Methods:
        - __str__: Returns the date as a string.

    Usage:
        date = Date("2022-01-01")
        print(date)  # Output: 2022-01-01
    """

    def __init__(self, date_str: Optional[str] = None):
        """
        Creates a Date instance that supports typing and validation for the format YYYY-MM-DD.

        :param date_str: Date in the format YYYY-MM-DD or None.
        """
        self.date: Optional[datetime] = None
        if date_str:
            self.date = self._validate_date(date_str)

    @staticmethod
    def _validate_date(date_str: str) -> datetime:
        """
        Validates that the date is in the format YYYY-MM-DD.

        :param date_str: Date as a string.
        :return: Validated date as a datetime instance.
        """
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError as exc:
            raise ValueError(
                f"Date must be in format YYYY-MM-DD, got: {date_str}"
            ) from exc

    def __str__(self) -> str:
        """
        Returns the date as a string in the format YYYY-MM-DD, or 'None' if not set.
        """
        return self.date.strftime("%Y-%m-%d") if self.date else "None"

    def is_set(self) -> bool:
        """
        Returns True if the date is set, otherwise False.
        """
        return self.date is not None

    def to_dict(self) -> Optional[str]:
        """
        Converts the Date object to a serializable format.
        :return: The date as a string in YYYY-MM-DD format, or None if not set.
        """
        return self.date.strftime("%Y-%m-%d") if self.date else None

    def to_json(self) -> Optional[str]:
        """
        Converts the Date object to a JSON serializable format.
        :return: The date as a string in YYYY-MM-DD format, or None if not set.
        """
        return self.to_dict()


class DateEncoder(json.JSONEncoder):
    """
    Date Encoder Class.

    This class is a custom JSON encoder that converts Date objects to strings.

    Methods:
        - default: Encodes a Date object as a string.

    Usage:
        encoder = DateEncoder()
        date = Date("2022-01-01")
        json_string = json.dumps(date, cls=encoder)
    """

    def default(self, o):
        if isinstance(o, Date):
            return o.to_json()
        return super().default(o)
