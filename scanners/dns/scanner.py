from time import perf_counter
from core.contracts.scanner import BaseScanner
from core.enums.scan import ScanStatus
from core.enums.scan import ScanType
from core.enums.scan import TargetType
from core.models.scan_context import ScanContext
from core.models.scan_error import ScanError
from core.models.scan_result import ScanResult

from core.models.requests.dns_request import DNSRequest
from core.models.configuration import Configuration

from scanners.dns.client import DNSClient
from scanners.dns.normalizer import DNSNormalizer
from scanners.dns.mapper import DNSMapper

from intelligence.dns.records import RecordsAnalyzer
from intelligence.dns.dnssec import DNSSECAnalyzer
from intelligence.dns.ptr import PTRAnalyzer
from intelligence.dns.mail import MailAnalyzer
from intelligence.dns.nameserver import NameServerAnalyzer


class DNSScanner(BaseScanner):

    NAME = "dns"

    REQUEST_MODEL = DNSRequest

    VERSION = "1.0.0"

    def __init__(self):

        self.client = DNSClient()

        self.normalizer = DNSNormalizer()

        self.mapper = DNSMapper()

        self.analyzers = [

            RecordsAnalyzer(),

            DNSSECAnalyzer(),

            PTRAnalyzer(),

            MailAnalyzer(),

            NameServerAnalyzer(),

        ]

    def scan(
        self,
        request: DNSRequest,
        configuration: Configuration,
    ) -> ScanResult:

        target_type = request.target.target_type

        start = perf_counter()

        context = ScanContext(

            target=request.target.original,

            target_type= target_type,

            scanner_name="DNS Scanner",

            scanner_version=self.VERSION,

            scan_type=ScanType.PASSIVE,

            duration_ms=0,

            configuration=configuration.model_dump(),

        )

        try:

            raw_data = self.client.query(

                request.target.domain,

                configuration,

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

                scanner="DNS Scanner",

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

                scanner="DNS Scanner",

                status=ScanStatus.FAILED,

                context=context,

                errors=[

                    ScanError(

                        error_type=type(exc).__name__,

                        message=str(exc),

                    )

                ],

            )
        
        