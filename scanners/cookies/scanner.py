from time import perf_counter

from core.models.scan_context import ScanContext
from core.models.scan_result import ScanResult
from core.models.scan_error import ScanError
from core.enums.scan import ScanStatus
from core.enums.scan import ScanType
from core.enums.scan import TargetType

from scanners.http.client import HTTPClient

from scanners.cookies.normalizer import CookieNormalizer
from scanners.cookies.mapper import CookieMapper

from intelligence.cookies.secure import SecureAnalyzer
from intelligence.cookies.httponly import HttpOnlyAnalyzer
from intelligence.cookies.samesite import SameSiteAnalyzer
from intelligence.cookies.expiration import ExpirationAnalyzer
from intelligence.cookies.prefix import PrefixAnalyzer

from urllib.parse import urlparse
from core.enums.scan import TargetType


class CookieScanner:

    VERSION = "1.0.0"

    def __init__(self):

        self.client = HTTPClient()

        self.normalizer = CookieNormalizer()

        self.mapper = CookieMapper()

        self.analyzers = [

            SecureAnalyzer(),

            HttpOnlyAnalyzer(),

            SameSiteAnalyzer(),

            ExpirationAnalyzer(),

            PrefixAnalyzer(),

        ]

    def scan(
        self,
        request,
        configuration,
    ) -> ScanResult:

        parsed = urlparse(request.target)

        if parsed.scheme and parsed.netloc:
            target_type = TargetType.URL
        else:
            target_type = TargetType.DOMAIN

        start = perf_counter()

        context = ScanContext(

            target=request.target,

            target_type=target_type,

            scanner_name="Cookie Scanner",

            scanner_version=self.VERSION,

            scan_type=ScanType.PASSIVE,

            duration_ms=0,

            configuration=configuration.model_dump(),

        )

        try:

            raw_data = self.client.query(
                request.target,
            )

            cookies = self.normalizer.normalize(
                raw_data,
            )

            findings = []

            for cookie in cookies:

                findings = []

                for cookie in cookies:

                    for analyzer in self.analyzers:

                        findings.extend(

                            analyzer.analyze(
                                cookie,
                            )

                        )

                findings = self.mapper.map(
                    findings,
                )

            context.duration_ms = (

                perf_counter() - start

            ) * 1000

            return ScanResult(

                scanner="Cookie Scanner",

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

                scanner="Cookie Scanner",

                status=ScanStatus.FAILED,

                context=context,

                errors=[

                    ScanError(

                        message=str(exc),

                    )

                ],

            )