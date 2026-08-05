from time import perf_counter

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
from intelligence.infrastructure.ptr import PTRAnalyzer
from intelligence.infrastructure.geo import GeoAnalyzer
from intelligence.infrastructure.provider import ProviderAnalyzer

class InfrastructureScanner:

    def __init__(self):

        self.client = InfrastructureClient()
        self.normalizer = InfrastructureNormalizer()
        self.mapper = InfrastructureMapper()
        self.analyzers = [

            ASNAnalyzer(),

            PTRAnalyzer(),

            GeoAnalyzer(),

            ProviderAnalyzer(),

        ]

    def scan(
        self,
        request: InfrastructureRequest,
        configuration: Configuration,
    ) -> ScanResult:

        start = perf_counter()

        context = ScanContext(
            target=request.target,
            target_type=TargetType.DOMAIN,
            scanner_name="infrastructure",
            scanner_version="1.0.0",
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
                scanner="infrastructure",
                status=ScanStatus.SUCCESS,
                context=context,
                findings=findings,
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