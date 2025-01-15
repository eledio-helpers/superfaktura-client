from typing import Dict

import requests
import os
from dotenv import load_dotenv  # type: ignore


class SuperFakturaAPIException(Exception):
    pass


class SuperFakturaAPI:
    def __init__(self) -> None:
        load_dotenv()
        _api_key = os.getenv("SUPERFAKTURA_API_KEY")
        self._api_url = os.getenv("SUPERFAKTURA_API_URL")
        _api_mail = os.getenv("SUPERFAKTURA_API_EMAIL")
        _api_company_id = os.getenv("SUPERFAKTURA_API_COMPANY_ID")
        self._auth_header = {
            "Authorization": f"SFAPI email={_api_mail}&apikey={_api_key}&company_id={_api_company_id}"
        }

    def get(self, endpoint: str) -> Dict:
        url = f"{self._api_url}/{endpoint}"
        req = requests.get(url=url, headers=self._auth_header)
        if req.status_code == 200:
            return req.json()
        else:
            raise SuperFakturaAPIException(
                f"Get status code: {req.status_code}; {req.json()}"
            )

    def post(self, endpoint: str, data: str) -> Dict:
        url = f"{self._api_url}/{endpoint}"
        req = requests.post(url=url, headers=self._auth_header, data={"data": data})
        if req.status_code == 200:
            return req.json()
        else:
            raise SuperFakturaAPIException(
                f"Post status code: {req.status_code}; {req.json()}"
            )
