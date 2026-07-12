from time import perf_counter

from core.contracts.scanner import BaseScanner
from core.models.configuration import Configuration
from core.models.scan_context import ScanContext
from core.models.scan_error import ScanError
from core.models.scan_result import ScanResult

from core.enums.scan import ScanStatus
from core.enums.scan import ScanType
from core.enums.scan import TargetType

from core.models.requests.whois_request import WHOISRequest

from scanners.whois.client import WHOISClient
from scanners.whois.normalizer import WHOISNormalizer
from scanners.whois.mapper import WHOISMapper


class WHOISScanner(BaseScanner):

    def __init__(self):

        self.client = WHOISClient()
        self.normalizer = WHOISNormalizer()
        self.mapper = WHOISMapper()

    def scan(
        self,
        request: WHOISRequest,
        configuration: Configuration,
    ) -> ScanResult:

        start = perf_counter()

        context = ScanContext(
            target=request.target,
            target_type=TargetType.DOMAIN,
            scanner_name="whois",
            scanner_version="1.0.0",
            scan_type=ScanType.PASSIVE,
            duration_ms=0,
            configuration=configuration.model_dump(),
        )

        try:

            raw_data = self.client.query(
                request.target,
            )

            normalized = self.normalizer.normalize(
                raw_data,
            )

            findings = self.mapper.map(
                normalized,
            )

            context.duration_ms = (perf_counter() - start) * 1000

            return ScanResult(
                scanner="whois",
                status=ScanStatus.SUCCESS,
                context=context,
                findings=findings,
                errors=[],
            )

        except Exception as e:

            context.duration_ms = (perf_counter() - start) * 1000

            return ScanResult(
                scanner="whois",
                status=ScanStatus.FAILED,
                context=context,
                findings=[],
                errors=[
                    ScanError(
                        error_type=type(e).__name__,
                        message=str(e),
                    )
                ],
            )