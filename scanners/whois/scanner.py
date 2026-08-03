from time import perf_counter

from core.enums.scan import ScanStatus
from core.enums.scan import ScanType
from core.enums.scan import TargetType

from core.models.scan_context import ScanContext
from core.models.scan_error import ScanError
from core.models.scan_result import ScanResult

from scanners.whois.client import WHOISClient
from scanners.whois.normalizer import WHOISNormalizer
from scanners.whois.mapper import WHOISMapper

from intelligence.whois.registrar import RegistrarAnalyzer
from intelligence.whois.dates import DatesAnalyzer
from intelligence.whois.privacy import PrivacyAnalyzer
from intelligence.whois.nameservers import NameServersAnalyzer
from intelligence.whois.status import StatusAnalyzer
from intelligence.whois.contacts import ContactsAnalyzer


class WHOISScanner:

    VERSION = "2.0.0"

    def __init__(self):

        self.client = WHOISClient()

        self.normalizer = WHOISNormalizer()

        self.mapper = WHOISMapper()

        self.analyzers = [

            RegistrarAnalyzer(),

            DatesAnalyzer(),

            PrivacyAnalyzer(),

            NameServersAnalyzer(),

            StatusAnalyzer(),

            ContactsAnalyzer(),

        ]

    def scan(
        self,
        request,
        configuration,
    ) -> ScanResult:

        start = perf_counter()

        context = ScanContext(

            target=request.target,

            target_type=TargetType.DOMAIN,

            scanner_name="WHOIS Scanner",

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

                scanner="WHOIS Scanner",

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

                scanner="WHOIS Scanner",

                status=ScanStatus.FAILED,

                context=context,

                errors=[

                    ScanError(

                        message=str(exc),

                    )

                ],

            )