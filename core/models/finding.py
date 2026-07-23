from typing import Any

from pydantic import BaseModel


class Finding(BaseModel):
    """
    One piece of information discovered by a scanner.

    A finding is always a FACT.
    It never contains severity or recommendations.
    """

    name: str

    category: str

    value: Any

    description: str | None = None

    entity: str | None = None

    metadata: dict[str, Any] = {}