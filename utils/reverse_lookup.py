import dns.resolver
import dns.reversename

def reverse_lookup(ip_address, dns_server):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [dns_server]
    reverse_name = dns.reversename.from_address(ip_address)
    return resolver.resolve(reverse_name, "PTR")
