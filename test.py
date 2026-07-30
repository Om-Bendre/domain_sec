from pprint import pprint

from core.models.configuration import Configuration
# from scanners.authentication.scanner import AuthenticationScanner
# from core.models.requests.authentication_request import AuthenticationRequest
from scanners.cookies.scanner import CookieScanner
from core.models.requests.cookie_request import CookieRequest

def main():

    request = CookieRequest(

        target="https://github.com/login",

    )

    scanner = CookieScanner()

    result = scanner.scan(request, Configuration())

    print("\n========== RAW DATA ==========\n")

    pprint(result.raw_data)

    print("\n========== FINDINGS ==========\n")

    for finding in result.findings:

        print(finding)


if __name__ == "__main__":

    main()