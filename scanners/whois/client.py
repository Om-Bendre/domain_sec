import whois


class WHOISClient:

    def query(
        self,
        domain: str,
    ):

        data = whois.whois(domain)

        return data