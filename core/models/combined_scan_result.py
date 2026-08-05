from pydantic import BaseModel, Field

from core.models.finding import Finding
from core.models.scan_result import ScanResult


class CombinedScanResult(BaseModel):
    """
    Represents the complete output of the orchestration layer.
    This becomes the single input to the Rule Engine.
    """

    target: str

    scan_results: list[ScanResult] = Field(
        default_factory=list,
    )

    findings: list[Finding] = Field(
        default_factory=list,
    )