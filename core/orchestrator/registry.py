from scanners.dns.scanner import DNSScanner
from scanners.whois.scanner import WHOISScanner
from scanners.http.scanner import HTTPScanner
from scanners.tls.scanner import TLSScanner
from scanners.security_headers.scanner import SecurityHeadersScanner
from scanners.cookies.scanner import CookieScanner


class ScannerRegistry:

    def get_scanners(self):

        return [

            DNSScanner(),

            WHOISScanner(),

            HTTPScanner(),

            TLSScanner(),

            SecurityHeadersScanner(),

            CookieScanner(),

        ]