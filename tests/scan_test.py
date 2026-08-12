from pprint import pprint

from core.models.configuration import Configuration

from core.models.requests.dns_request import DNSRequest
from core.models.requests.whois_request import WHOISRequest
from core.models.requests.http_request import HTTPRequest
from core.models.requests.tls_request import TLSRequest
from core.models.requests.security_headers_request import SecurityHeadersRequest
from core.models.requests.cookie_request import CookieRequest

from scanners.dns.scanner import DNSScanner
from scanners.whois.scanner import WHOISScanner
from scanners.http.scanner import HTTPScanner
from scanners.tls.scanner import TLSScanner
from scanners.security_headers.scanner import SecurityHeadersScanner
from scanners.cookies.scanner import CookieScanner



SCANNERS = [

    ("DNS", DNSScanner(), DNSRequest(target="google.com")),

    ("WHOIS", WHOISScanner(), WHOISRequest(target="google.com")),

    ("HTTP", HTTPScanner(), HTTPRequest(target="https://github.com")),

    ("TLS", TLSScanner(), TLSRequest(target="github.com")),

    ("Security Headers", SecurityHeadersScanner(), SecurityHeadersRequest(target="https://github.com")),

    ("Cookies", CookieScanner(), CookieRequest(target="https://github.com")),


]

configuration = Configuration()

for name, scanner, request in SCANNERS:

    print("\n" + "=" * 80)
    print(name)
    print("=" * 80)

    try:

        result = scanner.scan(
            request,
            configuration,
        )

        print(f"Status   : {result.status}")
        print(f"Fact : {len(result.Fact)}")
        print(f"Errors   : {len(result.errors)}")

        if result.errors:

            pprint(result.errors)

    except Exception as e:

        print("FAILED")
        print(type(e).__name__)
        print(e)