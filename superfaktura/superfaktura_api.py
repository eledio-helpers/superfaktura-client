"""
SuperFaktura API Client.

This module provides classes and functions for working with the SuperFaktura API.
It allows for reading, creating, updating, and deleting data in SuperFaktura.

Classes:
    - SuperFakturaAPI: The base class for working with the SuperFaktura API.
    - SuperFakturaAPIException: An exception for errors when working with the SuperFaktura API.
    - SuperFakturaAPIMissingCredentialsException: An exception for missing login credentials.

Functions:
    - get: Retrieves data from the SuperFaktura API.
    - post: Creates or updates data in the SuperFaktura API.

Usage:
    >>> import superfaktura.superfaktura_api
    >>> # Create an instance of SuperFakturaAPI
    >>> api = superfaktura.superfaktura_api.SuperFakturaAPI()
    >>> # Retrieve data from the SuperFaktura API
    >>> incoming_data = api.get('endpoint')
    >>> # Create or update data in the SuperFaktura API
    >>> api.post('endpoint', outgoing_data)
"""

import os
from typing import Dict, IO

import requests
from dotenv import load_dotenv  # type: ignore


class SuperFakturaAPIException(Exception):
    """Exception for errors when working with the SuperFaktura API."""


class SuperFakturaAPIMissingCredentialsException(Exception):
    """Exception for missing login credentials."""


class SuperFakturaAPI:
    """Base class for working with the SuperFaktura API."""

    def __init__(self) -> None:
        load_dotenv()
        _api_key = os.getenv("SUPERFAKTURA_API_KEY")
        self._api_url = os.getenv("SUPERFAKTURA_API_URL")
        _api_mail = os.getenv("SUPERFAKTURA_API_EMAIL")
        _api_company_id = os.getenv("SUPERFAKTURA_API_COMPANY_ID")
        if not _api_key or not self._api_url or not _api_mail or not _api_company_id:
            raise SuperFakturaAPIMissingCredentialsException(
                "Please ensure, that necessary "
                "credentials are set. Please see"
                " README.md"
            )

        self._auth_header = {
            "Authorization": f"SFAPI email={_api_mail}&apikey={_api_key}&company_id="
            f"{_api_company_id}"
        }

    def get(self, endpoint: str, timeout: int = 5) -> Dict:
        """
        Retrieves data from the SuperFaktura API.

        Retrieves data from the specified endpoint in the SuperFaktura API.

        Args:
            endpoint (str): The API endpoint to retrieve data from (e.g. 'invoices', 'clients',
                            etc.).
            timeout (int, optional): The timeout for the API request in seconds. Defaults to 5.

        Returns:
            Dict: The retrieved data in JSON format.

        Raises:
            SuperFakturaAPIException: If the API request fails or returns an error.

        Examples:
            >>> api = SuperFakturaAPI()
            >>> data = api.get('invoices')
            >>> print(data)

        Notes:
            The available endpoints can be found in the SuperFaktura API documentation.
        """
        url = f"{self._api_url}/{endpoint}"
        req = requests.get(url=url, headers=self._auth_header, timeout=timeout)
        if req.status_code == 200:
            try:
                return req.json()
            except requests.exceptions.JSONDecodeError as e:
                raise SuperFakturaAPIException(
                    f"Unable to decode response as JSON; {req.content!r}; {e}"
                ) from e
        raise SuperFakturaAPIException(
            f"Get status code: {req.status_code}; {req.content!r}"
        )

    def download(self, endpoint: str, descriptor: IO[bytes], timeout: int = 5) -> None:
        """
        Download data stream from the SuperFaktura API.

        Download data stream from the specified endpoint in the SuperFaktura API.

        Args:
            endpoint (str): The API endpoint to retrieve data from (e.g. 'invoices', 'clients',
                            etc.).
            descriptor (IO[bytes]): The descriptor to write the data stream to.
            timeout (int, optional): The timeout for the API request in seconds. Defaults to 5.

        Returns:
            None

        Raises:
            SuperFakturaAPIException: If the API request fails or returns an error.

        Examples:
            >>> from superfaktura.invoice import Invoice
            >>> from superfaktura.enumerations.language import Language
            >>> invoice = Invoice()
            >>> with open("invoice.pdf", "wb") as f:
            >>>     invoice.get_pdf(invoice=invoice_data, descriptor=f, language=Language.English)

        Notes:
            The available endpoints can be found in the SuperFaktura API documentation.
        """
        url = f"{self._api_url}/{endpoint}"
        req = requests.get(url=url, headers=self._auth_header, timeout=timeout)
        if req.status_code == 200:
            if descriptor.writable():
                descriptor.write(req.content)
            else:
                raise SuperFakturaAPIException(
                    f"Descriptor {descriptor} is not writable"
                )
        else:
            raise SuperFakturaAPIException(
                f"Download status code: {req.status_code}; {req.content!r}"
            )

    def post(self, endpoint: str, data: str, timeout: int = 5) -> Dict:
        """
        Creates or updates data in the SuperFaktura API.

        Creates or updates data in the specified endpoint in the SuperFaktura API.

        Args:
            endpoint (str): The API endpoint to create or update data in (e.g. 'invoices',
                            'clients', etc.).
            data (str): The data to be created or updated in JSON format.
            timeout (int, optional): The timeout for the API request in seconds. Defaults
                                    to 5.

        Returns:
            Dict: The created or updated data in JSON format.

        Raises:
            SuperFakturaAPIException: If the API request fails or returns an error.

        Examples:
            >>> api = SuperFakturaAPI()
            >>> data = '{"name": "Example Invoice", "amount": 100.0}'
            >>> response = api.post('invoices', data)
            >>> print(response)

        Notes:
            The available endpoints can be found in the SuperFaktura API documentation.
            The data should be a valid JSON string.
        """
        url = f"{self._api_url}/{endpoint}"
        req = requests.post(
            url=url, headers=self._auth_header, data={"data": data}, timeout=timeout
        )
        if req.status_code == 200:
            return req.json()
        raise SuperFakturaAPIException(
            f"Post status code: {req.status_code}; {req.json()}"
        )
