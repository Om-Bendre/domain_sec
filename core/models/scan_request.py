from pydantic import BaseModel

from core.models.resolved_target import ResolvedTarget


class ScanRequest(BaseModel):
    """
    Base request model for all scanners.
    """

    target: ResolvedTarget