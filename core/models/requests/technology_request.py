from pydantic import BaseModel


class TechnologyRequest(BaseModel):
    """
    Request model for the Technology Scanner.
    """

    target: str