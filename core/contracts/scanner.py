from abc import ABC, abstractmethod

from core.models.scan_result import ScanResult
from core.models.configuration import Configuration
from core.models.requests.scan_request import ScanRequest


class BaseScanner(ABC):
    """
    Base class for every SecureCheck scanner.
    """

    @abstractmethod
    def scan(
        self,
        request: ScanRequest,
        configuration: Configuration
    ) -> ScanResult:
        pass