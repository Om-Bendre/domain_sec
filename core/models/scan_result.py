from pydantic import BaseModel

from core.models.scan_context import ScanContext
from core.models.finding import Finding
from core.models.scan_error import ScanError
from core.models.enums import ScanStatus


class ScanResult(BaseModel):
    """
    Standard output returned by every SecureCheck scanner.
    """

    scanner: str

    status: ScanStatus

    context: ScanContext

    findings: list[Finding] = []

    errors: list[ScanError] = []