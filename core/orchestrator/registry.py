from scanners.dns.scanner import DNSScanner
from scanners.whois.scanner import WHOISScanner
from scanners.infrastructure.scanner import InfrastructureScanner
from scanners.http.scanner import HTTPScanner
from scanners.tls.scanner import TLSScanner
from scanners.security_headers.scanner import SecurityHeadersScanner
from scanners.cookies.scanner import CookieScanner
from scanners.authentication.scanner import AuthenticationScanner
from scanners.api.scanner import APIScanner
from scanners.technology.scanner import TechnologyScanner


class ScannerRegistry:

    def get_scanners(self):

        return [

            DNSScanner(),

            WHOISScanner(),

            InfrastructureScanner(),

            HTTPScanner(),

            TLSScanner(),

            SecurityHeadersScanner(),

            CookieScanner(),

            AuthenticationScanner(),

            APIScanner(),

            TechnologyScanner(),

        ]