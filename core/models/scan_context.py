from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class ScanContext(BaseModel):
    """
    Metadata describing one scan execution.
    Shared by every scanner.
    """

    target: str
    target_type: str

    scanner_name: str
    scanner_version: str

    scan_type: str

    started_at: datetime = Field(default_factory=datetime.utcnow)

    duration_ms: float

    configuration: dict[str, Any]