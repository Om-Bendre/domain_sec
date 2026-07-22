from pydantic import BaseModel


class SecurityHeadersRequest(BaseModel):
    """
    Request model for the Security Headers Scanner.
    """

    target: str