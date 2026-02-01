"""
Utility helpers for Scribe.

This module provides a centralized sanitizer to replace non-finite floats
(inf, -inf, NaN) with None before JSON serialization so PostgreSQL JSONB
parsing does not fail (it rejects tokens like Infinity).
"""
import math
from typing import Any

def replace_non_finite(obj: Any) -> Any:
    """Recursively replace non-finite floats (inf, -inf, NaN) with None.

    This prevents json.dumps from emitting non-standard tokens like Infinity
    which PostgreSQL JSONB parsing rejects.
    """
    if isinstance(obj, float):
        return obj if math.isfinite(obj) else None
    if isinstance(obj, dict):
        return {k: replace_non_finite(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [replace_non_finite(v) for v in obj]
    if isinstance(obj, tuple):
        return tuple(replace_non_finite(v) for v in obj)
    return obj
