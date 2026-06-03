"""Load .env from repository root (and optional PythonRpa/.env overrides)."""
from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

_REPO_ROOT = Path(__file__).resolve().parent.parent
_LOADED = False


def load_repo_env() -> Path:
    global _LOADED
    root_env = _REPO_ROOT / ".env"
    local_env = _REPO_ROOT / "PythonRpa" / ".env"
    load_dotenv(root_env)
    if local_env.exists():
        load_dotenv(local_env, override=True)
    _LOADED = True
    return root_env


def getenv(key: str, default: str = "") -> str:
    if not _LOADED:
        load_repo_env()
    return os.environ.get(key, default).strip()


def getenv_bool(key: str, default: bool = False) -> bool:
    if not _LOADED:
        load_repo_env()
    raw = os.environ.get(key)
    if raw is None or not str(raw).strip():
        return default
    val = str(raw).strip().lower()
    return val in ("1", "true", "yes", "on")


def getenv_int(key: str, default: int) -> int:
    raw = getenv(key, "")
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError:
        return default


def getenv_list(key: str, separator: str = ",") -> list[str]:
    raw = getenv(key, "")
    if not raw:
        return []
    return [part.strip() for part in raw.split(separator) if part.strip()]
