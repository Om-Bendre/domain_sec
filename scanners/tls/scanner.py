from time import perf_counter

from core.contracts.scanner import BaseScanner

from core.enums.scan import ScanStatus
from core.enums.scan import ScanType
from core.enums.scan import TargetType

from core.models.configuration import Configuration
from core.models.scan_context import ScanContext
from core.models.scan_error import ScanError
from core.models.scan_result import ScanResult

from core.models.requests.tls_request import TLSRequest

from scanners.tls.client import TLSClient
from scanners.tls.normalizer import TLSNormalizer
from scanners.tls.mapper import TLSMapper

from intelligence.tls.protocol import ProtocolAnalyzer
from intelligence.tls.cipher import CipherAnalyzer
from intelligence.tls.certificate import CertificateAnalyzer
from intelligence.tls.expiry import ExpiryAnalyzer
from intelligence.tls.issuer import IssuerAnalyzer

class TLSScanner(BaseScanner):

    def __init__(self):

        self.client = TLSClient()

        self.normalizer = TLSNormalizer()

        self.mapper = TLSMapper()

        self.intelligence_modules = [
            ProtocolAnalyzer(),

            CipherAnalyzer(),

            CertificateAnalyzer(),

            ExpiryAnalyzer(),

            IssuerAnalyzer(),
        ]

    def scan(
        self,
        request: TLSRequest,
        configuration: Configuration,
    ) -> ScanResult:

        start = perf_counter()

        context = ScanContext(
            target=request.target,
            target_type=TargetType.DOMAIN,
            scanner_name="tls",
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
                scanner="tls",
                status=ScanStatus.SUCCESS,
                context=context,
                findings=findings,
                raw_data={
                    "certificate": raw_data["certificate"],
                },
                errors=[],
            )

        except Exception as e:

            context.duration_ms = (
                perf_counter() - start
            ) * 1000

            return ScanResult(
                scanner="tls",
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