from time import perf_counter
from core.contracts.scanner import BaseScanner

from core.enums.scan import ScanStatus
from core.enums.scan import ScanType
from core.enums.scan import TargetType

from core.models.configuration import Configuration
from core.models.scan_context import ScanContext
from core.models.scan_error import ScanError
from core.models.scan_result import ScanResult

from core.models.requests.infrastructure_request import InfrastructureRequest

from scanners.infrastructure.client import InfrastructureClient
from scanners.infrastructure.normalizer import InfrastructureNormalizer
from scanners.infrastructure.mapper import InfrastructureMapper


from intelligence.infrastructure.asn import ASNAnalyzer

from intelligence.infrastructure.provider import ProviderAnalyzer

class InfrastructureScanner(BaseScanner):

    NAME = "infrastructure"

    REQUEST_MODEL = InfrastructureRequest

    VERSION = "1.0.0"

    def __init__(self):

        self.client = InfrastructureClient()
        self.normalizer = InfrastructureNormalizer()
        self.mapper = InfrastructureMapper()
        self.analyzers = [

            ASNAnalyzer(),

            ProviderAnalyzer(),

        ]

    def scan(
        self,
        request: InfrastructureRequest,
        configuration: Configuration,
    ) -> ScanResult:

        target_type = request.target.target_type

        start = perf_counter()

        context = ScanContext(
            target=request.target.original,
            target_type= target_type,
            scanner_name="infrastructure",
            scanner_version="1.0.0",
            scan_type=ScanType.PASSIVE,
            duration_ms=0,
            configuration=configuration.model_dump(),
        )

        try:

            raw_data = self.client.query(
                request.target.ip
                if request.target.ip
                else request.target.domain,
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
                scanner="infrastructure",
                status=ScanStatus.SUCCESS,
                context=context,
                fact=facts,
                raw_data= {},
                errors=[],
            )

        except Exception as e:

            context.duration_ms = (
                perf_counter() - start
            ) * 1000

            return ScanResult(
                scanner="infrastructure",
                status=ScanStatus.FAILED,
                context=context,
                errors=[
                    ScanError(
                        error_type=type(e).__name__,
                        message=str(e),
                    )
                ],
            )