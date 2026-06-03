"""ASIN extraction helpers."""
import re
from typing import Optional, Set
from urllib.parse import urlparse

_ASIN_RE = re.compile(r"(?:/dp/|/gp/product/|/product/)([A-Z0-9]{10})", re.I)
_ASIN_JSON_RE = re.compile(r'"asin"\s*:\s*"([A-Z0-9]{10})"', re.I)
_ASIN_DP_RE = re.compile(r"/dp/([A-Z0-9]{10})", re.I)

# プロモ・カード等（必要なら .env で拡張）
DEFAULT_BLOCKLIST_ASINS = frozenset({"B08P4CFBK6"})


def asin_from_href(href: Optional[str]) -> Optional[str]:
    if not href:
        return None
    match = _ASIN_RE.search(href)
    if match:
        return match.group(1).upper()
    path = urlparse(href).path
    match = _ASIN_RE.search(path)
    return match.group(1).upper() if match else None


def extract_asins_from_html(html: str, blocklist: Optional[Set[str]] = None) -> Set[str]:
    """HTML / page_source から ASIN を抽出（React 埋め込み JSON 向け）。"""
    block = blocklist or DEFAULT_BLOCKLIST_ASINS
    found: Set[str] = set()
    for pattern in (_ASIN_JSON_RE, _ASIN_DP_RE):
        for match in pattern.findall(html):
            asin = match.upper()
            if asin not in block:
                found.add(asin)
    return found


def dedupe_asin_records(records: list) -> list:
    seen = set()
    out = []
    for row in records:
        asin = row.get("asin") if isinstance(row, dict) else row
        if not asin or asin in seen:
            continue
        seen.add(asin)
        out.append(row)
    return out
