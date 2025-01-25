import tempfile
from typing import IO


def save_temporary_file_as_pdf(
    temp_file: IO[bytes], output_path: str = "output.pdf"
) -> None:
    with open(output_path, "wb") as f:
        f.write(temp_file.read())
        temp_file.close()
