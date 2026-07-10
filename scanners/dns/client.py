from utils.resolver import lookup
from utils.reverse_lookup import reverse_lookup
from utils.dnssec import check_dnssec


class DNSClient:
    """
    Wrapper around the legacy DNS resolver.
    Responsible only for collecting DNS data.
    """

    def query_forward(
        self,
        domain: str,
        record_type: str,
        resolver: str,
    ):

        results, ttl = lookup(
            domain,
            record_type,
            resolver,
        )

        return {
            "results": results,
            "ttl": ttl,
        }
    
    def query_reverse(
        self,
        ip_address: str,
        resolver: str,
    ):
        results = reverse_lookup(
            ip_address,
            resolver,
        )

        return {
            "results": results,
            "ttl": None,
        }
    
    def check_dnssec(
    self,
    domain: str,
    resolver: str,
    ):
        results = check_dnssec(domain, resolver)

        return {
            "results": results
        }
        