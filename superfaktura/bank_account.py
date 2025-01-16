from dataclasses import dataclass, asdict
from typing import Optional

from superfaktura.superfaktura_api import SuperFakturaAPI


class NoDefaultBankAccountException(Exception):
    pass


@dataclass
class BankAccountModel:
    account: Optional[str]
    bank_code: Optional[str]
    bank_name: Optional[str]
    default: Optional[int]
    iban: Optional[str]
    show: Optional[int]
    swift: Optional[str]
    id: Optional[int]

    def as_dict(self) -> dict:
        data = asdict(self)
        for key in list(data.keys()):
            if data[key] is None:
                del data[key]
        return data

    @staticmethod
    def from_dict(data: dict) -> "BankAccountModel":
        return BankAccountModel(
            **{
                k: v
                for k, v in data.items()
                if k in BankAccountModel.__dataclass_fields__
            }
        )


class BankAccount(SuperFakturaAPI):
    def __init__(self):
        super().__init__()

    def list(self) -> dict:
        url = "bank_accounts/index"
        return self.get(url)

    def default(self) -> Optional[BankAccountModel]:
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
