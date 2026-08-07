from abc import ABC
from abc import abstractmethod


class BaseScanner(ABC):

    NAME = ""

    REQUEST_MODEL = None

    VERSION = "1.0.0"

    @abstractmethod
    def scan(
        self,
        request,
        configuration,
    ):
        pass