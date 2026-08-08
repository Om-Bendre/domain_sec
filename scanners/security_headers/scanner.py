from time import perf_counter

from core.contracts.scanner import BaseScanner

from core.enums.scan import ScanStatus
from core.enums.scan import ScanType
from core.enums.scan import TargetType

from core.models.configuration import Configuration
from core.models.scan_context import ScanContext
from core.models.scan_error import ScanError
from core.models.scan_result import ScanResult

from core.models.requests.security_headers_request import (
    SecurityHeadersRequest,
)

from scanners.http.client import HTTPClient

from scanners.security_headers.normalizer import (
    SecurityHeadersNormalizer,
)

from scanners.security_headers.mapper import (
    SecurityHeadersMapper,
)

from intelligence.security_headers.hsts import (
    HSTSAnalyzer,
)

from intelligence.security_headers.csp import (
    CSPAnalyzer,
)

from intelligence.security_headers.xfo import (
    XFrameOptionsAnalyzer,
)

from intelligence.security_headers.xcto import (
    XContentTypeOptionsAnalyzer,
)

from intelligence.security_headers.referrer import (
    ReferrerPolicyAnalyzer,
)

from intelligence.security_headers.permissions import (
    PermissionsPolicyAnalyzer,
)


class SecurityHeadersScanner(BaseScanner):

    NAME = "security_headers"

    REQUEST_MODEL = SecurityHeadersRequest

    VERSION = "1.0.0"

    def __init__(self):

        self.client = HTTPClient()

        self.normalizer = SecurityHeadersNormalizer()

        self.mapper = SecurityHeadersMapper()

        self.analyzers = [
            HSTSAnalyzer(),
            CSPAnalyzer(),
            XFrameOptionsAnalyzer(),
            XContentTypeOptionsAnalyzer(),
            ReferrerPolicyAnalyzer(),
            PermissionsPolicyAnalyzer(),
        ]

    def scan(
        self,
        request: SecurityHeadersRequest,
        configuration: Configuration,
    ) -> ScanResult:

        target_type = request.target.target_type

        start = perf_counter()

        context = ScanContext(
            target=request.target.original,
            target_type= target_type,
            scanner_name="security_headers",
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

            for analyzer in self.analyzers:

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
                scanner="security_headers",
                status=ScanStatus.SUCCESS,
                context=context,
                findings=findings,
                raw_data= {},
                errors=[],
            )

        except Exception as e:

            context.duration_ms = (
                perf_counter() - start
            ) * 1000

            return ScanResult(
                scanner="security_headers",
                status=ScanStatus.FAILED,
                context=context,
                findings=[],
                raw_data={},
                errors=[
                    ScanError(
                        error_type=type(e).__name__,
                        message=str(e),
                    )
                ],
            )