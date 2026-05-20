import pytest
from pathlib import Path
from skillmaker.fetchers.pdf import extract_pdf_text


def test_raises_on_missing_file():
    with pytest.raises(FileNotFoundError):
        extract_pdf_text("/nonexistent/path/file.pdf")


def test_raises_on_wrong_extension(tmp_path):
    txt_file = tmp_path / "document.txt"
    txt_file.write_text("not a pdf")
    with pytest.raises(ValueError, match="must be a .pdf"):
        extract_pdf_text(str(txt_file))


def test_extracts_text_from_valid_pdf(tmp_path):
    from pypdf import PdfWriter
    writer = PdfWriter()
    writer.add_blank_page(width=612, height=792)
    pdf_path = tmp_path / "test.pdf"
    with open(pdf_path, "wb") as f:
        writer.write(f)
    result = extract_pdf_text(str(pdf_path))
    assert isinstance(result, str)
