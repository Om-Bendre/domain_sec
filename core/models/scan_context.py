from datetime import datetime
from typing import Any
from core.enums.scan import TargetType
from pydantic import BaseModel, Field
from core.enums.scan import ScanType


class ScanContext(BaseModel):
    """
    Metadata describing one scan execution.
    Shared by every scanner.
    """

    target: str
    target_type: TargetType

    scanner_name: str
    scanner_version: str

    scan_type: ScanType

    started_at: datetime = Field(default_factory=datetime.utcnow)

    duration_ms: float

    configuration: dict[str, Any]