import dataclasses
from pprint import pprint

from superfaktura.api import SuperFakturaAPI


@dataclasses.dataclass
class ClientContactModel:
    name: str
    address: str = None
    bank_account: str = None
    bank_code: str = None
    city: str = None
    comment: str = None
    country: str = None
    country_id: int = None
    currency: str = None
    default_variable: str = None
    delivery_address: str = None
    delivery_city: str = None
    delivery_country: str = None
    delivery_country_id: int = None
    delivery_name: str = None
    delivery_phone: str = None
    delivery_zip: str = None
    dic: str = None
    discount: float = None
    due_date: int = None
    email: str = None
    fax: str = None
    iban: str = None
    ic_dph: str = None
    ico: str = None
    match_address: int = None
    phone: str = None
    swift: str = None
    tags: str = None
    uuid: str = None
    zip: str = None
    update: bool = None


class ClientContact(SuperFakturaAPI):
    def __init__(self):
        super().__init__()

    def add_contact(self, contact: ClientContactModel):
        url = "clients/create"
        return self.post(endpoint=url, data=dataclasses.asdict(contact))

if __name__ == "__main__":
    client = ClientContact()
    resp = client.add_contact(ClientContactModel(name="John Doe"))
    pprint(resp)
