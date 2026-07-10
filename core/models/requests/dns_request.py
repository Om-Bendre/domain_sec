from core.models.requests.scan_request import ScanRequest
from core.enums.dns import DNSRecordType
from pydantic import Field

class DNSRequest(ScanRequest):
    """
    Request model for DNS scans.
    """

    record_type: DNSRecordType = DNSRecordType.A

    check_dnssec: bool = Field(default=False)
