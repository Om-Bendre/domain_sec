from time import perf_counter
from urllib.parse import urlparse

from core.enums.scan import ScanStatus
from core.enums.scan import ScanType
from core.enums.scan import TargetType

from core.models.scan_context import ScanContext
from core.models.scan_error import ScanError
from core.models.scan_result import ScanResult

from scanners.api.client import APISecurityClient
from scanners.api.normalizer import APISecurityNormalizer
from scanners.api.mapper import APISecurityMapper

from intelligence.api.authentication import AuthenticationAnalyzer
from intelligence.api.cors import CORSAnalyzer
from intelligence.api.methods import MethodsAnalyzer
from intelligence.api.versioning import VersioningAnalyzer
from intelligence.api.documentation import DocumentationAnalyzer
from intelligence.api.rate_limiting import RateLimitingAnalyzer
from intelligence.api.error_handling import ErrorHandlingAnalyzer
from intelligence.api.sensitive_data import SensitiveDataAnalyzer
from intelligence.api.api_characteristics import (
    APICharacteristicsAnalyzer,
)

class APISecurityScanner:

    VERSION = "1.0.0"

    def __init__(self):

        self.client = APISecurityClient()

        self.normalizer = APISecurityNormalizer()

        self.mapper = APISecurityMapper()

        self.analyzers = [

            AuthenticationAnalyzer(),

            CORSAnalyzer(),

            MethodsAnalyzer(),

            VersioningAnalyzer(),

            DocumentationAnalyzer(),

            RateLimitingAnalyzer(),

            ErrorHandlingAnalyzer(),

            SensitiveDataAnalyzer(),

            APICharacteristicsAnalyzer(),

        ]

    def scan(
        self,
        request,
        configuration,
    ) -> ScanResult:

        parsed = urlparse(
            request.target,
        )

        if parsed.scheme and parsed.netloc:

            target_type = TargetType.URL

        else:

            target_type = TargetType.DOMAIN

        start = perf_counter()

        context = ScanContext(

            target=request.target,

            target_type=target_type,

            scanner_name="API Security Scanner",

            scanner_version=self.VERSION,

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

                scanner="API Security Scanner",

                status=ScanStatus.SUCCESS,

                context=context,

                findings=findings,

                raw_data=raw_data,

            )

        except Exception as exc:

            context.duration_ms = (

                perf_counter() - start

            ) * 1000

            return ScanResult(

                scanner="API Security Scanner",

                status=ScanStatus.FAILED,

                context=context,

                errors=[

                    ScanError(

                        message=str(exc),

                    )

                ],

            )