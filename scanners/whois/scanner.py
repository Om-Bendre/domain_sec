from time import perf_counter
from core.contracts.scanner import BaseScanner
from core.enums.scan import ScanStatus
from core.enums.scan import ScanType
from core.enums.scan import TargetType

from core.models.scan_context import ScanContext
from core.models.scan_error import ScanError
from core.models.scan_result import ScanResult

from core.models.requests.whois_request import WHOISRequest
from core.models.configuration import Configuration

from scanners.whois.client import WHOISClient
from scanners.whois.normalizer import WHOISNormalizer
from scanners.whois.mapper import WHOISMapper

from intelligence.whois.registrar import RegistrarAnalyzer
from intelligence.whois.dates import DatesAnalyzer
from intelligence.whois.privacy import PrivacyAnalyzer

from intelligence.whois.status import StatusAnalyzer



class WHOISScanner(BaseScanner):

    NAME = "whois"

    REQUEST_MODEL = WHOISRequest

    VERSION = "1.0.0"

    def __init__(self):

        self.client = WHOISClient()

        self.normalizer = WHOISNormalizer()

        self.mapper = WHOISMapper()

        self.analyzers = [

            RegistrarAnalyzer(),

            DatesAnalyzer(),

            PrivacyAnalyzer(),

            StatusAnalyzer(),

            

        ]

    def scan(
        self,
        request: WHOISRequest,
        configuration: Configuration,
    ) -> ScanResult:

        target_type = request.target.target_type

        start = perf_counter()

        context = ScanContext(

            target=request.target.original,

            target_type= target_type,

            scanner_name="WHOIS Scanner",

            scanner_version=self.VERSION,

            scan_type=ScanType.PASSIVE,

            duration_ms=0,

            configuration=configuration.model_dump(),

        )

        try:

            raw_data = self.client.query(

                request.target.domain,

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

                scanner="WHOIS Scanner",

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

                scanner="WHOIS Scanner",

                status=ScanStatus.FAILED,

                context=context,

                errors=[

                    ScanError(

                        error_type=type(exc).__name__,
                        message=str(exc),

                    )

                ],

            )