import fitz  # PyMuPDF

def parse_resume_text(path: str) -> str:
    """Extracts raw text from a PDF resume. For text files, read raw content."""
    text = ""
    try:
        doc = fitz.open(path)
        for page in doc:
            text += page.get_text()
        doc.close()
    except Exception:
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                text = f.read()
        except Exception:
            text = ""
    text = ' '.join(text.split())
    return text
