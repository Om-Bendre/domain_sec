import ipaddress


def analyze_ipv6(ip):

    address = ipaddress.ip_address(ip)

    return {
        "version": address.version,
        "compressed": address.compressed,
        "exploded": address.exploded,
        "is_private": address.is_private,
        "is_global": address.is_global,
        "is_loopback": address.is_loopback,
        "is_multicast": address.is_multicast,
        "is_reserved": address.is_reserved,
        "is_link_local": address.is_link_local
    }