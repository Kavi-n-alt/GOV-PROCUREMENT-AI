import pdfplumber
import pandas as pd
import re
from pathlib import Path

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


def extract_basic_fields(text):
    data = {
        "tender_id": None,
        "department": None,
        "estimated_value": None
    }

    tender_id = re.search(r"Tender ID[:\s]*([A-Z0-9/-]+)", text)
    if tender_id:
        data["tender_id"] = tender_id.group(1)

    value = re.search(r"Estimated Value[:\s]*Rs\.?\s*([\d,]+)", text)
    if value:
        data["estimated_value"] = value.group(1).replace(",", "")

    return data


def process_pdf(pdf_path, output_csv):
    text = extract_text_from_pdf(pdf_path)
    record = extract_basic_fields(text)

    df = pd.DataFrame([record])
    df.to_csv(output_csv, index=False)


if __name__ == "__main__":
    pdf_path = "data/raw/sample.pdf"
    output_csv = "data/processed/cppp_tender.csv"
    process_pdf(pdf_path, output_csv)
