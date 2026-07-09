class DNSNormalizer:
    """
    Converts raw DNS client output into
    SecureCheck-friendly Python data.
    """

    def normalize(self, raw_data):

        normalized = []

        for record in raw_data["results"]:

            normalized.append(
                {
                    "record": str(record),
                    "ttl": raw_data["ttl"],
                }
            )

        return normalized