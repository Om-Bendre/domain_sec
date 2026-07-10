from core.models.requests.dns_request import DNSRequest
from core.enums.dns import DNSRecordType
from core.models.configuration import Configuration

from scanners.dns.scanner import DNSScanner


scanner = DNSScanner()

config = Configuration()

record_types = [

    # DNSRecordType.A,
    # DNSRecordType.AAAA,
    # DNSRecordType.MX,
    # DNSRecordType.NS,
    # DNSRecordType.TXT,
    # DNSRecordType.CNAME,
    # DNSRecordType.CAA,
    DNSRecordType.PTR,

]

for record in record_types:

    print(f"\n===== {record.value} =====")

    request = DNSRequest(

        target="8.8.8.8",

        record_type=DNSRecordType.PTR,

    )

    result = scanner.scan(
        request,
        config,
    )

    print(result.model_dump_json(indent=2))