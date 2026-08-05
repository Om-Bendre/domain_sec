from time import perf_counter

from core.enums.scan import ScanStatus
from core.enums.scan import ScanType
from core.enums.scan import TargetType

from core.models.configuration import Configuration
from core.models.scan_context import ScanContext
from core.models.scan_error import ScanError
from core.models.scan_result import ScanResult

from core.models.requests.http_request import HTTPRequest

from scanners.http.client import HTTPClient
from scanners.http.normalizer import HTTPNormalizer
from scanners.http.mapper import HTTPMapper

from intelligence.http.redirect import RedirectAnalyzer
from intelligence.http.server import ServerAnalyzer
from intelligence.http.compression import CompressionAnalyzer
from intelligence.http.caching import CacheAnalyzer
from intelligence.http.contents import ContentAnalyzer
from intelligence.http.version import HTTPVersionAnalyzer


class HTTPScanner:

    def __init__(self):

        self.client = HTTPClient()

        self.normalizer = HTTPNormalizer()

        self.mapper = HTTPMapper()

        self.intelligence_modules = [

            RedirectAnalyzer(),

            ServerAnalyzer(),

            CompressionAnalyzer(),

            CacheAnalyzer(),

            ContentAnalyzer(),

            HTTPVersionAnalyzer(),
        ]

    def scan(
        self,
        request: HTTPRequest,
        configuration: Configuration,
    ) -> ScanResult:

        start = perf_counter()

        context = ScanContext(
            target=request.target,
            target_type=TargetType.URL,
            scanner_name="http",
            scanner_version="1.0.0",
            scan_type=ScanType.PASSIVE,
            duration_ms=0,
            configuration=configuration.model_dump(),
        )

        try:

            raw_data = self.client.query(
                request.target,
            )

            normalized_data = self.normalizer.normalize(
                raw_data,
            )

            findings = []

            for analyzer in self.intelligence_modules:

                findings.extend(

                    analyzer.analyze(
                        normalized_data,
                    )

                )

            findings = self.mapper.map(
                findings,
            )

            context.duration_ms = (
                perf_counter() - start
            ) * 1000

            return ScanResult(
                scanner="http",
                status=ScanStatus.SUCCESS,
                context=context,
                findings=findings,
                raw_data={
                    "headers": raw_data["headers"],
                    "redirect_chain": raw_data["history"],
                },
                errors=[],
            )
        except Exception as e:

            context.duration_ms = (
                perf_counter() - start
            ) * 1000

            return ScanResult(
                scanner="http",
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