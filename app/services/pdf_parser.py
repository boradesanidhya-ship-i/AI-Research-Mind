import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from a PDF file using PyMuPDF
    """

    # Open PDF
    doc = fitz.open(pdf_path)

    extracted_text = ""

    # Read every page
    for page in doc:
        extracted_text += page.get_text()

    # Close document
    doc.close()

    return extracted_text