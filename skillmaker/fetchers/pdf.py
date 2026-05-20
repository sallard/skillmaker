from pathlib import Path
from pypdf import PdfReader


def extract_pdf_text(file_path: str) -> str:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {file_path}")
    if path.suffix.lower() != ".pdf":
        raise ValueError(f"File must be a .pdf, got: {path.suffix}")
    reader = PdfReader(str(path))
    pages = [page.extract_text() or "" for page in reader.pages]
    return "\n\n".join(pages).strip()
