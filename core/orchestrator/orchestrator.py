from core.models.configuration import Configuration
from core.models.requests.scan_request import ScanRequest
from scanners.dns.scanner import DNSScanner


class Orchestrator:

    def __init__(self):

        self.configuration = Configuration()

        self.scanners = {
            "dns": DNSScanner(),
        }

    def run(
        self,
        scanner_name: str,
        request: ScanRequest,
    ):

        scanner = self.scanners.get(scanner_name)

        if scanner is None:
            raise ValueError(
                f"Unknown scanner: {scanner_name}"
            )

        return scanner.scan(
            request,
            self.configuration
        )