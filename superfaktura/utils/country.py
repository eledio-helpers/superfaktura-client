from pprint import pprint

from superfaktura.superfaktura_api import SuperFakturaAPI


def country_list():
    api = SuperFakturaAPI()
    url = "countries"
    return api.get(url)


pprint(country_list())
