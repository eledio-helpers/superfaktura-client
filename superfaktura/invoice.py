from dataclasses import dataclass, asdict
from typing import Optional, List
import json

from superfaktura.bank_account import BankAccount
from superfaktura.client_contacts import ClientContactModel
from superfaktura.enumerations.currency import Currencies
from superfaktura.superfaktura_api import SuperFakturaAPI
from superfaktura.utils.data_types import Date, DateEncoder


@dataclass
class InvoiceModel:
    add_rounding_item: Optional[int] = 0
    already_paid: Optional[int] = None
    bank_accounts: Optional[List[dict]] = None
    comment: Optional[str] = None
    constant: Optional[str] = None
    created: Optional[Date] = None
    delivery: Optional[Date] = None
    delivery_type: Optional[str] = None
    deposit: Optional[float] = None
    discount: Optional[float] = 0
    discount_total: Optional[float] = None
    due: Optional[Date] = None
    estimate_id: Optional[int] = None
    header_comment: Optional[str] = None
    internal_comment: Optional[str] = None
    invoice_currency: Optional[str] = None
    invoice_no_formatted: Optional[str] = None
    issued_by: Optional[str] = None
    issued_by_email: Optional[str] = None
    issued_by_phone: Optional[str] = None
    issued_by_web: Optional[str] = None
    logo_id: Optional[int] = None
    mark_sent: Optional[int] = None
    mark_sent_message: Optional[str] = None
    mark_sent_subject: Optional[str] = None
    name: Optional[str] = None
    order_no: Optional[str] = None
    parent_id: Optional[int] = None
    paydate: Optional[Date] = None
    payment_type: Optional[str] = None
    proforma_id: Optional[str] = None
    rounding: Optional[str] = None
    sequence_id: Optional[int] = None
    specific: Optional[str] = None
    tax_document: Optional[int] = None
    type: Optional[str] = None
    variable: Optional[str] = None
    vat_transfer: Optional[int] = None

    def as_dict(self) -> dict:
        data = asdict(self)
        for key in list(data.keys()):
            if data[key] is None:
                del data[key]
        return data

    def to_dict(self) -> dict:
        """
        Converts the Record object to a dictionary for JSON serialization.
        """
        return {"due": self.due.to_dict() if self.due else None}


@dataclass
class InvoiceItem:
    name: str
    unit_price: float
    description: Optional[str] = None
    discount: Optional[float] = 0
    discount_description: Optional[str] = None
    load_data_from_stock: int = 0
    quantity: Optional[float] = 1
    sku: Optional[str] = None
    stock_item_id: Optional[int] = None
    tax: Optional[float] = None
    unit: Optional[str] = None
    use_document_currency: Optional[int] = 0

    def as_dict(self) -> dict:
        data = asdict(self)
        for key in list(data.keys()):
            if data[key] is None:
                del data[key]
        return data


class InvoiceType:
    PROFORMA = "proforma"
    INVOICE = "regular"


class Invoice(SuperFakturaAPI):
    def __init__(self):
        super().__init__()

    def add(
        self,
        invoice: InvoiceModel,
        items: List[InvoiceItem],
        contact: ClientContactModel,
    ):
        data = {
            "Invoice": invoice.as_dict(),
            "InvoiceItem": [item.as_dict() for item in items],
            "Client": contact.as_dict(),
        }
        url = "invoices/create"
        resp = self.post(endpoint=url, data=json.dumps(data, cls=DateEncoder))
        return resp


if __name__ == "__main__":
    invoice = Invoice()
    bank = BankAccount()
    invoice.add(
        invoice=InvoiceModel(
            type=InvoiceType.PROFORMA,
            name="Invoice 3",
            due=Date("2025-02-01"),
            invoice_currency=Currencies.CZK,
            header_comment="We invoice you for services",
            bank_accounts=[bank.default().as_dict()],
        ),
        items=[
            InvoiceItem(name="Services", unit_price=100, quantity=1, unit="ks", tax=21),
            InvoiceItem(name="SIM card", unit_price=50, quantity=1, tax=21, unit="ks"),
            InvoiceItem(
                name="SIM card 2", unit_price=75, quantity=1, tax=21, unit="ks"
            ),
        ],
        contact=ClientContactModel(
            name="Richard Kubíček",
            email="kubicekr@eledio.com",
            phone="+420 123 456 789",
            address="Jaroslava Foglara 861/1",
            ico="123",
            update=True,
            country_id=57,
        ),
    )
