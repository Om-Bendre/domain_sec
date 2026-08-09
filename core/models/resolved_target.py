from pydantic import BaseModel

from core.enums.scan import TargetType


class ResolvedTarget(BaseModel):
    """
    Canonical representation of the user's target.
    Every scanner receives this object.
    """

    original: str

    target_type: TargetType

    url: str | None = None

    domain: str | None = None

    ip: str | None = None