"""
This module contains tools for working with these examples.
"""


def save_file_as_pdf(input_data: bytes, output_path: str = "output.pdf") -> None:
    """
    Save the input data as a PDF file.
    :param input_data:
    :param output_path:
    :return:
    """
    with open(output_path, "wb") as f:
        f.write(input_data)
