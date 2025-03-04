"""
Bank Account Module.

This module provides classes and functions for working with bank accounts in the SuperFaktura API.
It allows for retrieving, creating, updating, and deleting bank accounts.

Classes:
    - BankAccountModel: Dataclass representing a bank account.
    - BankAccount: Class for interacting with bank accounts.

Exceptions:
    - NoDefaultBankAccountException: Exception for when no default bank account is found.

Functions:
    - (none)

Usage:
    >>> import superfaktura.bank_account
    >>> # Create an instance of BankAccount
    >>> bank = superfaktura.bank_account.BankAccount()
    >>> # Retrieve a list of bank accounts
    >>> accounts = bank.list()
    >>> # Get the default bank account
    >>> default_account = bank.default()
    >>> # Create or update a bank account
    >>> data = {"account": "1234567890", "bank_code": "1234567890", "default": True}
    >>> bank.post(data)
"""

from dataclasses import dataclass, asdict
from typing import Optional

from superfaktura.superfaktura_api import SuperFakturaAPI


class NoDefaultBankAccountException(Exception):
    """Exception for when no default bank account is found."""


@dataclass
class BankAccountModel:
    """Dataclass representing a bank account."""

    account: Optional[str]
    bank_code: Optional[str]
    bank_name: Optional[str]
    default: Optional[int]
    iban: Optional[str]
    show: Optional[int]
    swift: Optional[str]
    id: Optional[int]

    def as_dict(self) -> dict:
        """Returns a dictionary representation of the BankAccountModel."""
        data = asdict(self)
        for key in list(data.keys()):
            if data[key] is None:
                del data[key]
        return data

    @staticmethod
    def from_dict(data: dict) -> "BankAccountModel":
        """Creates a BankAccountModel from a dictionary."""
        return BankAccountModel(
            **{k: v for k, v in data.items() if k in BankAccountModel.__annotations__}
        )


class BankAccount(SuperFakturaAPI):
    """
    Bank Account Class.

    This class provides methods for interacting with bank accounts in the SuperFaktura API.
    It allows for retrieving, creating, updating, and deleting bank accounts.

    Methods:
        - list: Retrieves a list of bank accounts.
        - default: Retrieves the default bank account.
        - post: Creates or updates a bank account.

    Usage:
        >>> bank = BankAccount()
        >>> accounts = bank.list()
        >>> default_account = bank.default()
        >>> data = {"account": "1234567890", "bank_code": "1234567890", "default": True}
        >>> bank.post(data)
    """

    def __init__(self):
        super().__init__()

    def list(self) -> dict:
        """Retrieves a list of bank accounts."""
        url = "bank_accounts/index"
        return self.get(url)

    def default(self) -> Optional[BankAccountModel]:
        """Retrieves the default bank account."""
        accounts = self.list()["BankAccounts"]
        for account in accounts:
            if account["BankAccount"]["default"]:
                return BankAccountModel.from_dict(account["BankAccount"])
        raise NoDefaultBankAccountException("No default bank account found")


if __name__ == "__main__":
    bank = BankAccount()
    from pprint import pprint

    pprint(bank.list())
    pprint(bank.default())
