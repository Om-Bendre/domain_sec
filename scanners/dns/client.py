import dns.resolver
import dns.reversename


class DNSClient:
    """
    Responsible only for communicating with DNS servers.
    """

    def query_forward(
        self,
        domain: str,
        record_type: str,
        dns_server: str,
    ):

        resolver = dns.resolver.Resolver()
        resolver.nameservers = [dns_server]

        answer = resolver.resolve(domain, record_type)

        return {
            "type": "records",
            "results": answer,
            "ttl": answer.rrset.ttl,
        }

    def query_reverse(
        self,
        ip_address: str,
        dns_server: str,
    ):

        resolver = dns.resolver.Resolver()
        resolver.nameservers = [dns_server]

        reverse_name = dns.reversename.from_address(ip_address)

        answer = resolver.resolve(reverse_name, "PTR")

        return {
            "type": "records",
            "results": answer,
            "ttl": answer.rrset.ttl if answer.rrset else None,
        }

    def check_dnssec(
        self,
        domain: str,
        dns_server: str,
    ):

        resolver = dns.resolver.Resolver()
        resolver.nameservers = [dns_server]

        try:

            answer = resolver.resolve(domain, "DNSKEY")

            return {
                "type": "dnssec",
                "enabled": True,
                "dnskeys": answer,
            }

        except dns.resolver.NoAnswer:

            return {
                "type": "dnssec",
                "enabled": False,
                "dnskeys": None,
            }

        except dns.resolver.NXDOMAIN:
            raise