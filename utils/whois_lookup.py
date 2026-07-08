import whois
def lookup_whois(domain):
    """
    Perform a WHOIS lookup for a domain.

    Returns:
        python-whois result object
    """

    return whois.whois(domain)