from typing import Any

from pydantic import BaseModel, Field


class Rule(BaseModel):
    id: str
    category: str
    entity: str
    description: str
    condition: dict[str, Any]
    severity: str
    remediation: str
    references: list[str] = Field(default_factory=list)
