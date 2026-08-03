from core.models.configuration import Configuration

# Change these two imports
from core.models.requests.dns_request import DNSRequest
from scanners.dns.scanner import DNSScanner


configuration = Configuration()

scanner = DNSScanner()

request = DNSRequest(
    target="google.com",
)

result = scanner.scan(
    request,
    configuration,
)

print("\nStatus")
print(result.status)

print("\nErrors")

if result.errors:

    for error in result.errors:

        print(f"\nType    : {error.error_type}")
        print(f"Message : {error.message}")

else:

    print("No Errors")