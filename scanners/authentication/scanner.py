from time import perf_counter


from core.contracts.scanner import BaseScanner

from core.enums.scan import ScanStatus
from core.enums.scan import ScanType
from core.enums.scan import TargetType

from core.models.scan_context import ScanContext
from core.models.scan_error import ScanError
from core.models.scan_result import ScanResult

from core.models.requests.authentication_request import AuthenticationRequest
from core.models.configuration import Configuration

from scanners.authentication.client import AuthenticationClient
from scanners.authentication.normalizer import AuthenticationNormalizer
from scanners.authentication.mapper import AuthenticationMapper

from intelligence.authentication.login_form import LoginFormAnalyzer
from intelligence.authentication.session import SessionAnalyzer
from intelligence.authentication.csrf import CSRFAnalyzer
from intelligence.authentication.jwt import JWTAnalyzer
from intelligence.authentication.oauth import OAuthAnalyzer
from intelligence.authentication.mfa import MFAAnalyzer
from intelligence.authentication.password import PasswordAnalyzer


class AuthenticationScanner(BaseScanner):

    NAME = "authentication"

    REQUEST_MODEL = AuthenticationRequest

    VERSION = "1.0.0"

    def __init__(self):

        self.client = AuthenticationClient()

        self.normalizer = AuthenticationNormalizer()

        self.mapper = AuthenticationMapper()

        self.analyzers = [

            LoginFormAnalyzer(),

            SessionAnalyzer(),

            CSRFAnalyzer(),

            JWTAnalyzer(),

            OAuthAnalyzer(),

            MFAAnalyzer(),

            PasswordAnalyzer(),

        ]

    def scan(
        self,
        request: AuthenticationRequest,
        configuration: Configuration,
    ) -> ScanResult:

        target_type = request.target.target_type

        start = perf_counter()

        context = ScanContext(

            target=request.target.original,

            target_type=target_type,

            scanner_name="Authentication Scanner",

            scanner_version=self.VERSION,

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

            facts = []

            for analyzer in self.analyzers:

                facts.extend(

                    analyzer.analyze(

                        normalized_data,

                    )

                )

            facts = self.mapper.map(

                facts,

            )

            context.duration_ms = (

                perf_counter() - start

            ) * 1000

            return ScanResult(

                scanner="Authentication Scanner",

                status=ScanStatus.SUCCESS,

                context=context,

                fact=facts,

                raw_data= {},

            )

        except Exception as exc:

            context.duration_ms = (

                perf_counter() - start

            ) * 1000

            return ScanResult(

                scanner="Authentication Scanner",

                status=ScanStatus.FAILED,

                context=context,

                errors=[

                    ScanError(

                        error_type=type(exc).__name__,

                        message=str(exc),

                    )

                ],

            )