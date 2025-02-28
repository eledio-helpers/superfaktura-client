

def save_temporary_file_as_pdf(
    input_data: bytes, output_path: str = "output.pdf"
) -> None:
    with open(output_path, "wb") as f:
        f.write(input_data)
