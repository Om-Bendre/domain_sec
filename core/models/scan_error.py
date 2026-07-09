from typing import Any

from pydantic import BaseModel


class ScanError(BaseModel):
    """
    Represents one error encountered during a scan.
    """
    error_type: str
    message: str
    details: dict[str, Any] = {}