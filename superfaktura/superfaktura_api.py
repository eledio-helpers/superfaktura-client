from typing import Dict

import requests
import os
from dotenv import load_dotenv  # type: ignore

from superfaktura.enumerations.data_format import DataFormat


class SuperFakturaAPIException(Exception):
    pass


class SuperFakturaAPIMissingCredentialsException(Exception):
    pass


class SuperFakturaAPI:
    def __init__(self) -> None:
        load_dotenv()
        _api_key = os.getenv("SUPERFAKTURA_API_KEY")
        self._api_url = os.getenv("SUPERFAKTURA_API_URL")
        _api_mail = os.getenv("SUPERFAKTURA_API_EMAIL")
        _api_company_id = os.getenv("SUPERFAKTURA_API_COMPANY_ID")
        if not _api_key or not self._api_url or not _api_mail or not _api_company_id:
            raise SuperFakturaAPIMissingCredentialsException(
                "Please ensure, that necessary credentials are set. Please see README.md"
            )

        self._auth_header = {
            "Authorization": f"SFAPI email={_api_mail}&apikey={_api_key}&company_id={_api_company_id}"
        }

    def get(self, endpoint: str, data_format: DataFormat = DataFormat.JSON) -> Dict:
        """
        Sends a GET request to the specified endpoint and returns the response in the specified format.

        :param endpoint: The API endpoint to send the GET request to.
        :param data_format: The format in which to return the response. Defaults to JSON.
        :return: The response from the API in the specified format.
        :raises SuperFakturaAPIException: If the request fails or returns a non-200 status code.
        """
        url = f"{self._api_url}/{endpoint}"
        req = requests.get(url=url, headers=self._auth_header)
        if req.status_code == 200:
            if data_format == DataFormat.JSON:
                return req.json()
            elif data_format == DataFormat.PDF:
                return {"pdf": req.content}  # returns a dict with the PDF content
        else:
            raise SuperFakturaAPIException(
                f"Get status code: {req.status_code}; {req.json()}"
            )

    def post(self, endpoint: str, data: str) -> Dict:
        """
        Sends a POST request to the specified endpoint with the provided data.

        :param endpoint: The API endpoint to send the POST request to.
        :param data: The data to be sent in the POST request.
        :return: The response from the API in JSON format.
        :raises SuperFakturaAPIException: If the request fails or returns a non-200 status code.
        """
        url = f"{self._api_url}/{endpoint}"
        req = requests.post(url=url, headers=self._auth_header, data={"data": data})
        if req.status_code == 200:
            return req.json()
        else:
            raise SuperFakturaAPIException(
                f"Post status code: {req.status_code}; {req.json()}"
            )
