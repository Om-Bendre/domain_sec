from time import perf_counter

import dns.resolver

from core.contracts.scanner import BaseScanner
from core.models.configuration import Configuration
from core.models.scan_context import ScanContext
from core.models.scan_result import ScanResult
from core.models.scan_error import ScanError
from core.enums.dns import DNSRecordType
from core.enums.scan import ScanStatus
from core.enums.scan import ScanType
from core.enums.scan import TargetType
from core.models.requests.dns_request import DNSRequest

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
        request: DNSRequest,
        configuration: Configuration,
    ) -> ScanResult:

        start = perf_counter()

        context = ScanContext(
            target=request.target,
            target_type=(
                TargetType.IP
                if request.record_type == DNSRecordType.PTR
                else TargetType.DOMAIN
            ),
            scanner_name="dns",
            scanner_version="1.0.0",
            scan_type=ScanType.PASSIVE,
            duration_ms=0,
            configuration=configuration.model_dump(),
        )

        record_type = request.record_type.value

        try:
           if request.check_dnssec:

            raw_data = self.client.check_dnssec(
                request.target,
                configuration.resolver,
            )

           elif request.record_type == DNSRecordType.PTR:
            raw_data = self.client.query_reverse(
                request.target,
                configuration.resolver,
            )
           else:
            raw_data = self.client.query_forward(
                request.target,
                request.record_type.value,
                configuration.resolver,
            )

           normalized = self.normalizer.normalize(raw_data)

           findings = self.mapper.map(
               normalized,
               record_type,
           )

           context.duration_ms = (perf_counter() - start) * 1000

           return ScanResult(
                scanner="dns",
                status=ScanStatus.SUCCESS,
                context=context,
                findings=findings,
                errors=[],
           )

        except dns.resolver.NoAnswer:

            context.duration_ms = (perf_counter() - start) * 1000

            return ScanResult(
                scanner="dns",
                status=ScanStatus.FAILED,
                context=context,
                findings=[],
                errors=[
                    ScanError(
                        error_type="NoAnswer",
                        message=f"No {record_type} record found for {request.target}",
                    )
                ],
            )

        except dns.resolver.NXDOMAIN:

            context.duration_ms = (perf_counter() - start) * 1000

            return ScanResult(
                scanner="dns",
                status=ScanStatus.FAILED,
                context=context,
                findings=[],
                errors=[
                    ScanError(
                        error_type="NXDOMAIN",
                        message=f"Domain '{request.target}' does not exist.",
                    )
                ],
            )

        except dns.resolver.Timeout:

            context.duration_ms = (perf_counter() - start) * 1000

            return ScanResult(
                scanner="dns",
                status=ScanStatus.FAILED,
                context=context,
                findings=[],
                errors=[
                    ScanError(
                        error_type="Timeout",
                        message="DNS query timed out.",
                    )
                ],
            )

        except Exception as e:

            context.duration_ms = (perf_counter() - start) * 1000

            return ScanResult(
                scanner="dns",
                status=ScanStatus.FAILED,
                context=context,
                findings=[],
                errors=[
                    ScanError(
                        error_type=type(e).__name__,
                        message=str(e),
                    )
                ],
            )