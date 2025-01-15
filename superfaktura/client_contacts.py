import dataclasses
import json
from pprint import pprint
from typing import Optional

from superfaktura.superfaktura_api import SuperFakturaAPI


class ClientException(Exception):
    pass


@dataclasses.dataclass
class ClientContactModel:
    name: str
    address: Optional[str] = None
    bank_account: Optional[str] = None
    bank_code: Optional[str] = None
    city: Optional[str] = None
    comment: Optional[str] = None
    country: Optional[str] = None
    country_id: Optional[int] = None
    currency: Optional[str] = None
    default_variable: Optional[str] = None
    delivery_address: Optional[str] = None
    delivery_city: Optional[str] = None
    delivery_country: Optional[str] = None
    delivery_country_id: Optional[int] = None
    delivery_name: Optional[str] = None
    delivery_phone: Optional[str] = None
    delivery_zip: Optional[str] = None
    dic: Optional[str] = None
    discount: Optional[float] = None
    due_date: Optional[int] = None
    email: Optional[str] = None
    fax: Optional[str] = None
    iban: Optional[str] = None
    ic_dph: Optional[str] = None
    ico: Optional[str] = None
    match_address: Optional[int] = None
    phone: Optional[str] = None
    swift: Optional[str] = None
    tags: Optional[str] = None
    uuid: Optional[str] = None
    zip: Optional[str] = None
    update: Optional[bool] = None

    id: Optional[int] = None

    def as_dict(self) -> dict:
        data = dataclasses.asdict(self)
        for key in list(data.keys()):
            if data[key] is None:
                del data[key]
        return data

    @staticmethod
    def from_dict(data: dict) -> "ClientContactModel":
        return ClientContactModel(
            **{
                k: v
                for k, v in data.items()
                if k in ClientContactModel.__dataclass_fields__
            }
        )


class ClientContact(SuperFakturaAPI):
    def __init__(self):
        super().__init__()

    def add_contact(self, contact: ClientContactModel) -> bool:
        url = "clients/create"
        data = {"Client": contact.as_dict()}
        resp = self.post(endpoint=url, data=json.dumps(data))
        if resp["error_message"] == "Client created":
            return True
        return False

    def list(self) -> dict:
        url = "clients/index.json"
        return self.get(endpoint=url)

    def get_client(self, client_id: int) -> ClientContactModel:
        url = f"clients/view/{client_id}"
        data = self.get(endpoint=url)
        if "Client" not in data:
            raise ClientException("Client not found")
        data = data["Client"]
        return ClientContactModel.from_dict(data)


if __name__ == "__main__":
    client = ClientContact()
    resp = client.list()

    pprint(resp)

    pprint(client.get_client(40019))
