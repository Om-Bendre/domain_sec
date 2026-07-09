from time import perf_counter

from core.contracts.scanner import BaseScanner
from core.models.configuration import Configuration
from core.models.scan_context import ScanContext
from core.models.scan_result import ScanResult
from core.enums.scan import ScanStatus
from core.enums.scan import ScanType
from core.enums.scan import TargetType

from scanners.dns.client import DNSClient
from scanners.dns.normalizer import DNSNormalizer
from scanners.dns.mapper import DNSMapper


class DNSScanner(BaseScanner):

    def __init__(self):

        self.client = DNSClient()

        self.normalizer = DNSNormalizer()

        self.mapper = DNSMapper()

    def scan(
        self,
        target: str,
        configuration: Configuration,
    ) -> ScanResult:

        start = perf_counter()

        raw_data = self.client.query(
            target,
            "A",
            configuration.resolver,
        )

        normalized = self.normalizer.normalize(
            raw_data
        )

        findings = self.mapper.map(
            normalized,
            "A",
        )

        duration = (perf_counter() - start) * 1000

        context = ScanContext(
            target=target,
            target_type=TargetType.DOMAIN,
            scanner_name="dns",
            scanner_version="1.0.0",
            scan_type=ScanType.PASSIVE,
            duration_ms=duration,
            configuration=configuration.model_dump(),
        )

        return ScanResult(
            scanner="dns",
            status=ScanStatus.SUCCESS,
            context=context,
            findings=findings,
        )