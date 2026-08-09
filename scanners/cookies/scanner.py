from time import perf_counter

from core.contracts.scanner import BaseScanner

from core.models.scan_context import ScanContext
from core.models.scan_result import ScanResult
from core.models.scan_error import ScanError

from core.enums.scan import ScanStatus
from core.enums.scan import ScanType

from core.models.requests.cookie_request import CookieRequest
from core.models.configuration import Configuration

from scanners.http.client import HTTPClient

from scanners.cookies.normalizer import CookieNormalizer
from scanners.cookies.mapper import CookieMapper

from intelligence.cookies.secure import SecureAnalyzer
from intelligence.cookies.httponly import HttpOnlyAnalyzer
from intelligence.cookies.samesite import SameSiteAnalyzer
from intelligence.cookies.expiration import ExpirationAnalyzer
from intelligence.cookies.prefix import PrefixAnalyzer


class CookieScanner(BaseScanner):

    NAME = "cookies"

    REQUEST_MODEL = CookieRequest

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
        request: CookieRequest,
        configuration: Configuration,
    ) -> ScanResult:

        target_type = request.target.target_type

        start = perf_counter()

        context = ScanContext(

            target=request.target.original,

            target_type=target_type,

            scanner_name="Cookie Scanner",

            scanner_version=self.VERSION,

            scan_type=ScanType.PASSIVE,

            duration_ms=0,

            configuration=configuration.model_dump(),

        )

        try:

            raw_data = self.client.query(
                request.target.url,
            )

            cookies = self.normalizer.normalize(
                raw_data,
            )

            #
            # Deduplicate cookie instances
            #
            # A cookie is identified by:
            # name + domain + path
            #

            unique_cookies = []

            seen = set()

            for cookie in cookies:

                attributes = cookie.get(
                    "attributes",
                    {},
                )

                identity = (

                    cookie.get("name"),

                    attributes.get("domain"),

                    attributes.get("path"),

                )

                if identity in seen:

                    continue

                seen.add(identity)

                unique_cookies.append(
                    cookie
                )

            #
            # Analyze cookies
            #

            findings = []

            for cookie in unique_cookies:

                for analyzer in self.analyzers:

                    findings.extend(

                        analyzer.analyze(
                            cookie,
                        )

                    )

            #
            # Map findings
            #

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

                raw_data={},

                errors=[],

            )

        except Exception as exc:

            context.duration_ms = (

                perf_counter() - start

            ) * 1000

            return ScanResult(

                scanner="Cookie Scanner",

                status=ScanStatus.FAILED,

                context=context,

                findings=[],

                raw_data={},

                errors=[

                    ScanError(

                        error_type=type(exc).__name__,

                        message=str(exc),

                    )

                ],

            )