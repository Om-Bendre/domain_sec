def print_results(domain, record_type, results, ttl):

    print("\n==============================")
    print(f"{record_type} Records for {domain}")
    print("==============================\n")

    for index, data in enumerate(results, start=1):
        print(f"{index}. {data}")

    print(f"\nTTL : {ttl} seconds")

def print_reverse_results(ip_address, results):

    print(f"\nPTR Records for {ip_address}\n")

    for index, data in enumerate(results, start=1):
        print(f"{index}. {data}")

def print_ptr_intelligence(intel):
    """
    Display enriched PTR intelligence analysis.
    intel is the dict returned by analyze_ptr()
    """
    print("\n--- PTR Intelligence ---\n")

    if intel['provider']:
        print(f"  Provider   : {intel['icon']} {intel['provider']}")
        print(f"  Category   : {intel['category']}")
    else:
        print("  Provider   : Unrecognized")

    if intel['encoded_ip']:
        print(f"  Encoded IP : {intel['encoded_ip']}")

    if intel['region']:
        print(f"  Region     : {intel['region']}")

    if intel['service_hint']:
        print(f"  Service    : {intel['service_hint']}")

    print(f"  Confidence : {intel['confidence']}")
    print()

def print_dnssec_info(domain, enabled, dnskeys):
    print("\n==============================")
    print("DNSSEC Information")
    print("==============================\n")

    print(f"Domain : {domain}")

    if enabled:
        print("DNSSEC : Enabled\n")

        print("DNSKEY Records:\n")

        for index, key in enumerate(dnskeys, start=1):
            print(f"{index}. {key}")

    else:
        print("DNSSEC : Not Detected")

def print_whois_info(info):

    print("\n==============================")
    print("WHOIS Information")
    print("==============================\n")

    print(f"Domain      : {info.domain_name}")
    print(f"Registrar   : {info.registrar}")
    print(f"Created     : {info.creation_date}")
    print(f"Expires     : {info.expiration_date}")
    print(f"Updated     : {info.updated_date}")

    print("\nName Servers:")

    if info.name_servers:
        for server in sorted(info.name_servers):
            print(f"  • {server}")

def print_asn_info(ip_address, info):

    print("\n==============================")
    print("ASN Information")
    print("==============================\n")

    print(f"IP Address   : {ip_address}")
    print(f"ASN          : {info['asn']}")
    print(f"Organization : {info['organization']}")
    print(f"CIDR         : {info['cidr']}")
    print(f"Country      : {info['country']}")

def print_geoip_info(ip, geo):

    print("\n==============================")
    print("GeoIP Information")
    print("==============================\n")

    print(f"IP Address : {ip}")
    print(f"Country    : {geo['country']}")
    print(f"Region     : {geo['region']}")
    print(f"City       : {geo['city']}")
    print(f"ISP        : {geo['isp']}")
    print(f"Organization : {geo['organization']}")

def print_ipv6_info(info):

    print("\n==============================")
    print("IPv6 Analysis")
    print("==============================\n")

    print(f"Version      : IPv{info['version']}")
    print(f"Compressed   : {info['compressed']}")
    print(f"Expanded     : {info['exploded']}")
    print(f"Global       : {info['is_global']}")
    print(f"Private      : {info['is_private']}")
    print(f"Loopback     : {info['is_loopback']}")
    print(f"Multicast    : {info['is_multicast']}")
    print(f"Reserved     : {info['is_reserved']}")
    print(f"Link Local   : {info['is_link_local']}")