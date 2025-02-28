"""
This module contains tools for working with these examples.
"""

from pathlib import Path


def save_file_as_pdf(input_data: bytes, output_path: str = "output.pdf") -> None:
    """
    Save the input data as a PDF file.
    :param input_data:
    :param output_path:
    :return:
    """
    p = Path(output_path)
    p.write_bytes(input_data)
