from core.models.configuration import Configuration

# Change these two imports
from core.models.requests.http_request import HTTPRequest
from scanners.http.scanner import HTTPScanner


configuration = Configuration()

scanner = HTTPScanner()

request = HTTPRequest(
    target="https://google.com",
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