from abc import ABC, abstractmethod

from core.models.scan_result import ScanResult
from core.models.configuration import Configuration


class BaseScanner(ABC):
    """
    Base class for every SecureCheck scanner.
    """

    @abstractmethod
    def scan(
        self,
        target: str,
        configuration: Configuration
    ) -> ScanResult:
        """
        Execute a scan.

        Must return a ScanResult.
        """
        pass