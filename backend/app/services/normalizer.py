from typing import Dict


def normalize(raw: Dict) -> Dict:
    """Convert raw extracted data into a normalized tender dict.
    This is a small placeholder; replace with structured parsing rules.
    """
    text = raw.get("raw_text") or ""
    title = text.splitlines()[0][:120] if text else raw.get("filename")
    return {
        "title": title,
        "description": text[:1000],
        "raw": raw,
    }
