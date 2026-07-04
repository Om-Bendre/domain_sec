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
