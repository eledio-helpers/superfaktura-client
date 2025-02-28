"""
This script retrieves and prints the list of countries using the SuperFaktura API.
"""

from pprint import pprint

from superfaktura.utils.country import country_list


def main():
    """
    Main function to retrieve and print the list of countries using the SuperFaktura API.
    """
    pprint(country_list())


if __name__ == "__main__":
    main()
