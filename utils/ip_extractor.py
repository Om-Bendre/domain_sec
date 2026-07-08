
def extract_ips(results, record_type):
    """
    Extract IP addresses from DNS lookup results.
    Only A and AAAA records directly contain IP addresses.
    Returns a list of IP address strings.
    """
    ips = []

    if record_type in ("A", "AAAA"):
        for record in results:
            ips.append(str(record))

    return ips