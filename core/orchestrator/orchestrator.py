from core.enums.scan import TargetType

from core.models.configuration import Configuration
from core.models.combined_scan_result import CombinedScanResult

from core.orchestrator.target_resolver import TargetResolver
from core.orchestrator.registry import ScannerRegistry
from core.orchestrator.request_factory import RequestFactory

from core.models.exceptions import InvalidTargetError


class Orchestrator:

    def __init__(self):

        self.target_resolver = TargetResolver()

        self.registry = ScannerRegistry()

        self.request_factory = RequestFactory()

    def scan(
        self,
        target: str,
        configuration: Configuration,
    ) -> CombinedScanResult:

        # Resolve Target

        resolved_target = self.target_resolver.resolve(
            target,
        )

        if resolved_target.target_type == TargetType.INVALID:

            raise InvalidTargetError(
                f"'{target}' is not a valid target."
            )

        # Execute scanners
        
        # scan_results = []

        findings = []

        for scanner in self.registry.get_scanners():

            request = self.request_factory.create(

                scanner,

                resolved_target,

            )

            result = scanner.scan(

                request,

                configuration,

            )

            # scan_results.append(

            #     result,

            # )

            findings.extend(

                result.findings,

            )

        # Build combined result

        return CombinedScanResult(

            target=resolved_target.original,

            # scan_results=scan_results,

            findings=findings,

        )