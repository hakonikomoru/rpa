"""Repository-local paths for Amazon RPA scripts."""
from pathlib import Path

AMAZON_DIR = Path(__file__).resolve().parent
PYTHON_RPA_DIR = AMAZON_DIR.parent
OUTPUT_DIR = PYTHON_RPA_DIR / "outPutFile"


def asins_csv_for_date(date_str: str) -> Path:
    """Daily ASIN log: outPutFile/asinsYYYY-MM-DD.csv"""
    return OUTPUT_DIR / f"asins{date_str}.csv"


def ensure_output_dir() -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    return OUTPUT_DIR
