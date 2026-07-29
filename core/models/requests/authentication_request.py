from pydantic import BaseModel


class AuthenticationRequest(BaseModel):
    """
    Request model for Authentication Scanner.
    """

    target: str