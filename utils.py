import pandas as pd
from pypdf import PdfReader

def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text.strip()


def extract_text_from_csv(uploaded_file):
    try:
        # ✅ Correct parameter name
        df = pd.read_csv(uploaded_file, encoding="utf-8", encoding_errors="ignore")
    except TypeError:
        # 🔁 Fallback for older pandas versions
        df = pd.read_csv(uploaded_file)

    text = "CSV Data Summary:\n"
    text += f"Columns: {', '.join(df.columns)}\n\n"

    for idx, row in df.head(20).iterrows():
        text += f"Row {idx + 1}: {row.to_dict()}\n"

    return text.strip()
