"""
Main script to add an invoice and save it as a PDF using the SuperFaktura API.

This script demonstrates how to create an invoice with multiple items,
retrieve the invoice as a PDF, and save the PDF to a file.

Usage:
    Run this script directly to create and save an invoice PDF.

Dependencies:
    - examples.tools.save_file_as_pdf
    - superfaktura.bank_account.BankAccount
    - superfaktura.client_contacts.ClientContactModel
    - superfaktura.enumerations.currency.Currencies
    - superfaktura.enumerations.language.Language
    - superfaktura.invoice.Invoice
    - superfaktura.invoice.InvoiceModel
    - superfaktura.invoice.InvoiceType
    - superfaktura.invoice.InvoiceItem
    - superfaktura.invoice.InvoiceSettings
    - superfaktura.utils.data_types.Date
"""

from superfaktura.bank_account import BankAccount, NoDefaultBankAccountException
from superfaktura.client_contacts import ClientContactModel
from superfaktura.enumerations.currency import Currencies
from superfaktura.enumerations.language import Language
from superfaktura.invoice import (
    Invoice,
    InvoiceModel,
    InvoiceType,
    InvoiceItem,
    InvoiceSettings,
)
from superfaktura.utils.data_types import Date


def main():
    """
    Main function to add Invoice and save it as a pdf using the SuperFaktura API.
    """
    invoice = Invoice()
    bank = BankAccount()
    try:
        # Get default bank account
        bank_account = bank.default().as_dict()
    except NoDefaultBankAccountException as e:
        print(f"Error getting default bank account: {e}")
        bank_account = {}
    resp = invoice.add(
        invoice_model=InvoiceModel(
            type=InvoiceType.INVOICE,
            name="My First Invoice",
            due=Date("2025-04-01"),
            invoice_currency=Currencies.EUR,
            header_comment="We invoice you for services",
            bank_accounts=[bank_account],
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
        invoice_settings=InvoiceSettings(language=Language.English),
    )

    with open("invoice.pdf", "wb") as f:
        invoice.get_pdf(invoice=resp, descriptor=f, language=Language.English)


if __name__ == "__main__":
    main()
