"""
Invoice Module.

This module provides classes and functions for working with invoices in the SuperFaktura API.
It allows for retrieving, creating, updating, and deleting invoices.

Classes:
    - InvoiceModel: Dataclass representing an invoice.
    - InvoiceItem: Dataclass representing an invoice item.
    - Invoice: Class for interacting with invoices.

Exceptions:
    - NoDefaultBankAccountException: Exception for when no default bank account is found.

Functions:
    - (none)

Usage:
    >>> import superfaktura.invoice
    >>> # Create an instance of Invoice
    >>> invoice = superfaktura.invoice.Invoice()
    >>> # Create an invoice
    >>> invoice.add(
        invoice_model=InvoiceModel(
            type=InvoiceType.INVOICE,
            name="My First Invoice",
            due=Date("2025-04-01"),
            invoice_currency=Currencies.EUR,
            header_comment="We invoice you for services",
            bank_accounts=[bank.default().as_dict()],
        ),
        items=[
            InvoiceItem(
                name="Website Development", unit_price=1000.0, quantity=1, tax=20
            ),
            InvoiceItem(
                name="Hosting Service (1 year)", unit_price=500.0, quantity=1, tax=20
            ),
        ],
        contact=ClientContactModel(
            name="John Doe",
            email="john.doe@examle.com",
            phone="+1 555-1234",
            address="123 Main Street, New York",
            ico="987654321",
            update=True,
            country_id=225,
        ),
    )
"""

from dataclasses import dataclass, asdict
from typing import Optional, List, IO
import json

from superfaktura.client_contacts import ClientContactModel
from superfaktura.enumerations.language import Language
from superfaktura.superfaktura_api import SuperFakturaAPI
from superfaktura.utils.data_types import Date, DateEncoder


@dataclass
class InvoiceModel:
    """This dataclass represents an invoice in the SuperFaktura API."""

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
        """Returns a dictionary representation of the InvoiceModel."""
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
    """This dataclass represents an invoice item in the SuperFaktura API."""

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
        """Returns a dictionary representation of the InvoiceItem."""
        data = asdict(self)
        for key in list(data.keys()):
            if data[key] is None:
                del data[key]
        return data


@dataclass
class InvoiceRespModel:
    """
    This dataclass represents the response model for an invoice in the SuperFaktura API.

    Attributes:
        - error (int): The error code.
        - error_message (str): The error message.
        - invoice_id (Optional[int]): The ID of the invoice.
        - invoice_token (Optional[str]): The token of
    """

    error: int
    error_message: str
    invoice_id: Optional[int] = None
    invoice_token: Optional[str] = None


@dataclass
class InvoiceSettings:
    """
    This dataclass represents the settings for an invoice in the SuperFaktura API.
    """

    language: Optional[str] = None
    bysquare: Optional[bool] = None
    callback_payment: Optional[str] = None
    online_payment: Optional[bool] = None
    payment_info: Optional[bool] = None
    paypal: Optional[bool] = None
    show_prices: Optional[bool] = None
    signature: Optional[bool] = None
    summary_bg_color: Optional[str] = None

    def as_dict(self) -> dict:
        """Returns a dictionary representation of the ClientContactModel."""
        data = asdict(self)
        for key in list(data.keys()):
            if data[key] is None:
                del data[key]
        return data


class InvoiceType:
    """
    Invoice Type Enumeration.

    This enumeration represents the different types of invoices that can be created.

    Usage:
        invoice_type = InvoiceType.PROFORMA
    """

    PROFORMA = "proforma"
    INVOICE = "regular"


class Invoice(SuperFakturaAPI):
    """
    Invoice Class.

    This class provides methods for interacting with invoices in the SuperFaktura API.
    It allows for retrieving, creating, updating, and deleting invoices.

    Methods:
        - add: Creates a new invoice.
        - get: Retrieves an invoice by ID.
        - list: Retrieves a list of invoices.
        - update: Updates an existing invoice.

    Usage:
        >>> invoice = Invoice()
        >>> invoice.add(
            invoice_model=InvoiceModel(
                type=InvoiceType.INVOICE,
                name="My First Invoice",
                due=Date("2025-04-01"),
                invoice_currency=Currencies.EUR,
                header_comment="We invoice you for services",
                bank_accounts=[bank.default().as_dict()],
            ),
            items=[
                InvoiceItem(
                    name="Website Development", unit_price=1000.0, quantity=1, tax=20
                ),
                InvoiceItem(
                    name="Hosting Service (1 year)", unit_price=500.0, quantity=1, tax=20
                ),
            ],
            contact=ClientContactModel(
                name="John Doe",
                email="john.doe@examle.com",
                phone="+1 555-1234",
                address="123 Main Street, New York",
                ico="987654321",
                update=True,
                country_id=225,
            ),
        )
    """

    def __init__(self):
        super().__init__()

    def add(
        self,
        invoice_model: InvoiceModel,
        items: List[InvoiceItem],
        contact: ClientContactModel,
        invoice_settings: Optional[InvoiceSettings] = None,
    ) -> InvoiceRespModel:
        """
        Adds a new invoice.

        Args:
            invoice_model (InvoiceModel): The invoice model.
            items (List[InvoiceItem]): List of invoice items.
            contact (ClientContactModel): The client contact model.
            invoice_settings (Optional[InvoiceSettings]): The invoice settings.

        Returns:
            InvoiceRespModel: The response model for the invoice.
            :param invoice_settings:
            :param contact:
            :param items:
            :param invoice_model:
        """
        data = {
            "Invoice": invoice_model.as_dict(),
            "InvoiceItem": [item.as_dict() for item in items],
            "Client": contact.as_dict(),
            "InvoiceSetting": invoice_settings.as_dict() if invoice_settings else {},
        }
        url = "invoices/create"
        resp = self.post(endpoint=url, data=json.dumps(data, cls=DateEncoder))
        invoice_resp = InvoiceRespModel(
            error=resp["error"], error_message=resp["error_message"]
        )
        if "data" in resp:
            if "Invoice" in resp["data"]:
                invoice_resp.invoice_id = int(resp["data"]["Invoice"]["id"])
                invoice_resp.invoice_token = resp["data"]["Invoice"]["token"]
        return invoice_resp

    def get_pdf(
        self,
        invoice: InvoiceRespModel,
        descriptor: IO[bytes],
        language: str = Language.Czech,
    ) -> None:
        """
        Retrieves the PDF of the invoice.

        Args:
            invoice (InvoiceRespModel): The response model for the invoice.
            descriptor (IO[bytes]): The descriptor to write the PDF data to.
            language (str): The language for the PDF.

        Returns:
            None
        """
        url = f"{language}/invoices/pdf/{invoice.invoice_id}/token:{invoice.invoice_token}"
        self.download(url, descriptor)
