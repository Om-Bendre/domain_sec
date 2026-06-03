import dns.resolver
import dns.reversename

def reverse_lookup(ip_address):

    reverse_name = dns.reversename.from_address(ip_address)
    result = dns.resolver.resolve(reverse_name, "PTR")
    return result