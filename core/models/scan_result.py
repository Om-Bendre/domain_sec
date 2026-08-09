from pydantic import BaseModel
from typing import Any
from core.models.scan_context import ScanContext
from core.models.finding import Finding
from core.models.scan_error import ScanError
from core.enums.scan import ScanStatus


class ScanResult(BaseModel):
    """
    Standard output returned by every SecureCheck scanner.
    """

    scanner: str

    status: ScanStatus

    context: ScanContext

    findings: list[Finding] = []

    raw_data: dict = {}

    errors: list[ScanError] = []