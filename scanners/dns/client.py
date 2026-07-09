from utils.resolver import lookup


class DNSClient:
    """
    Wrapper around the legacy DNS resolver.
    Responsible only for collecting DNS data.
    """

    def query(
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