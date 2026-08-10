from pydantic import BaseModel, Field

from core.models.fact import Fact
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

    fact: list[Fact] = Field(
        default_factory=list,
    )