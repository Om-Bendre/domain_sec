from pydantic import BaseModel


class Configuration(BaseModel):
    """
    Global scanner configuration.
    Every scanner receives this object.
    """

    resolver: str = "1.1.1.1"

    timeout: int = 5

    retries: int = 2

    user_agent: str = "SecureCheck/1.0"

    verify_tls: bool = True