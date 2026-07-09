from abc import ABC, abstractmethod

from core.models.scan_result import ScanResult


class BaseIntelligence(ABC):
    """
    Base class for all SecureCheck intelligence modules.
    """

    @abstractmethod
    def analyze(self, result: ScanResult) -> ScanResult:
        """
        Enrich scan findings without assigning severity
        or risk scores.
        """
        pass