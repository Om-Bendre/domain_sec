from typing import Any

from pydantic import BaseModel, Field


class ScanRequest(BaseModel):
    """
    Represents a request to execute a scan.
    """

    target: str

    options: dict[str, Any] = Field(default_factory=dict)