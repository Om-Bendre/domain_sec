import dns.resolver

# def lookup(domain, record_type):
#     result = dns.resolver.resolve(domain, record_type)
#     return result

def lookup(domain, record_type, dns_server):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [dns_server]
    return resolver.resolve(domain, record_type)
