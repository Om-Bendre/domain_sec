from pydantic import BaseModel


class CookieRequest(BaseModel):
    """
    Request model for the Cookie Security Scanner.
    """

    target: str