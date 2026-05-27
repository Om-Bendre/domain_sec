import dns.resolver

def lookup(domain, record_type):
    result = dns.resolver.resolve(domain, record_type)
    return result
