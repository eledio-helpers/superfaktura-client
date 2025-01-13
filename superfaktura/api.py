from typing import Dict

import requests
import os
from dotenv import load_dotenv  # type: ignore


class SuperFakturaAPI:
    def __init__(self) -> None:
        load_dotenv()
        _api_key = os.getenv("SUPERFAKTURA_API_KEY")
        self._api_url = os.getenv("SUPERFAKTURA_API_URL")
        _api_mail = os.getenv("SUPERFAKTURA_API_EMAIL")
        self._auth_header = {
            "Authorization": f"SFAPI email={_api_mail}&apikey={_api_key}"
        }

    def get(self, endpoint: str) -> Dict:
        url = f"{self._api_url}/{endpoint}"
        req = requests.get(url=url, headers=self._auth_header)
        return req.json()

    def post(self, endpoint: str, data: dict) -> Dict:
        url = f"{self._api_url}/{endpoint}"
        print(url)
        print(data)
        req = requests.post(url=url, headers=self._auth_header, data=data)
        return req.json()
