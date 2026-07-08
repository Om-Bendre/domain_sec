from ipwhois import IPWhois
def lookup_asn(ip_address):
    obj = IPWhois(ip_address)
    result = obj.lookup_rdap()
    return result