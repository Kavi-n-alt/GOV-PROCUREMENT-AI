from typing import List, Dict


def deduplicate(tenders: List[Dict]) -> List[Dict]:
    """Simple deduplication stub based on exact raw text hash.
    Replace with a better fingerprinting approach for production.
    """
    seen = set()
    out = []
    for t in tenders:
        key = t.get("raw", {}).get("raw_text")
        if key in seen:
            continue
        seen.add(key)
        out.append(t)
    return out
