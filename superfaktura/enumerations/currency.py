"""
Currency Enumeration.

This module provides an enumeration of currencies that can be used in the SuperFaktura API.

Classes:
    - Currencies: Enumeration of currencies.

Usage:
    from superfaktura.enumerations.currency import Currencies
    currency = Currencies.CZK
"""


class Currencies:
    """
    Currency Enumeration.

    This enumeration represents the different currencies that can be used in the SuperFaktura API.

    Values:
        - CZK: Czech Koruna
        - EUR: Euro

    Usage:
        currency = Currencies.CZK
    """

    CZK = "CZK"
    EUR = "EUR"
