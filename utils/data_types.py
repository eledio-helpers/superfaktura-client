from datetime import datetime
from typing import Optional

import json


class Date:
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
        except ValueError:
            raise ValueError(f"Date must be in format YYYY-MM-DD, got: {date_str}")

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
    def default(self, o):
        if isinstance(o, Date):
            return o.to_json()
        return super().default(o)
