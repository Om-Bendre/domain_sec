from typing import Any

from pydantic import BaseModel, Field


class Fact(BaseModel):
    category: str
    entity: str | None = None
    name: str
    value: Any = None

    description: str | None = None

    evidence: str | None = None

    metadata: dict[str, Any] = Field(
        default_factory=dict,
    )