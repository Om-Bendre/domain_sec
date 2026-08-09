from time import perf_counter
from core.contracts.scanner import BaseScanner
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


from intelligence.http.version import HTTPVersionAnalyzer


class HTTPScanner(BaseScanner):

    NAME = "http"

    REQUEST_MODEL = HTTPRequest

    VERSION = "1.0.0"

    def __init__(self):

        self.client = HTTPClient()

        self.normalizer = HTTPNormalizer()

        self.mapper = HTTPMapper()

        self.intelligence_modules = [

            RedirectAnalyzer(),

            ServerAnalyzer(),

            CompressionAnalyzer(),

            HTTPVersionAnalyzer(),
        ]

    def scan(
        self,
        request: HTTPRequest,
        configuration: Configuration,
    ) -> ScanResult:

        target_type = request.target.target_type

        start = perf_counter()

        context = ScanContext(
            target=request.target.original,
            target_type= target_type,
            scanner_name="http",
            scanner_version="1.0.0",
            scan_type=ScanType.PASSIVE,
            duration_ms=0,
            configuration=configuration.model_dump(),
        )

        try:

            raw_data = self.client.query(
                request.target.url,
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
                raw_data={},
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