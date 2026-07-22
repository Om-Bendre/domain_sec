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

from intelligence.security_headers.hsts_analyzer import (
    HSTSAnalyzer,
)

from intelligence.security_headers.csp_analyzer import (
    CSPAnalyzer,
)

from intelligence.security_headers.xfo_analyzer import (
    XFrameOptionsAnalyzer,
)

from intelligence.security_headers.xcto_analyzer import (
    XContentTypeOptionsAnalyzer,
)

from intelligence.security_headers.referrer_analyzer import (
    ReferrerPolicyAnalyzer,
)

from intelligence.security_headers.permissions_analyzer import (
    PermissionsPolicyAnalyzer,
)


class SecurityHeadersScanner(BaseScanner):

    def __init__(self):

        self.client = HTTPClient()

        self.normalizer = SecurityHeadersNormalizer()

        self.mapper = SecurityHeadersMapper()

        self.intelligence_modules = [
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

        start = perf_counter()

        context = ScanContext(
            target=request.target,
            target_type=TargetType.DOMAIN,
            scanner_name="security_headers",
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

            for module in self.intelligence_modules:

                normalized.update(
                    module.analyze(
                        normalized,
                    )
                )

            findings = self.mapper.map(
                normalized,
            )

            context.duration_ms = (
                perf_counter() - start
            ) * 1000

            return ScanResult(
                scanner="security_headers",
                status=ScanStatus.SUCCESS,
                context=context,
                findings=findings,
                raw_data=raw_data,
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