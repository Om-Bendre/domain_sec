from pydantic import BaseModel


class APIRequest(BaseModel):
    """
    Request model for the API Security Scanner.
    """

    target: str