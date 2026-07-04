import dns.resolver

def check_dnssec(domain, dns_server):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [dns_server]
    try:
        answer = resolver.resolve(domain, "DNSKEY")
        return True, answer
    except dns.resolver.NoAnswer:
        return False, None
    except dns.resolver.NXDOMAIN:
        raise