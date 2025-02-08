"""
Country Module.

This module provides utilities for working with countries in the SuperFaktura API.

Functions:
    - country_list: Retrieves a list of countries.

Usage:
    from superfaktura.utils.country import country_list
    countries = country_list()
    print(countries)
"""

from superfaktura.superfaktura_api import SuperFakturaAPI


def country_list():
    """
    Retrieves a list of countries.

    This function returns a list of countries that can be used in the SuperFaktura API.

    Returns:
        - list: A list of countries.

    Usage:
        countries = country_list()
        print(countries)
    """
    api = SuperFakturaAPI()
    url = "countries"
    return api.get(url)
