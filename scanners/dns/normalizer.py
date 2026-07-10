class DNSNormalizer:

    def normalize(self, raw_data):

        if raw_data["type"] == "dnssec":

            return {
                "type": "dnssec",
                "enabled": raw_data["enabled"],
                "dnskeys": raw_data["dnskeys"],
            }

        normalized = []

        for record in raw_data["results"]:

            normalized.append({
                "record": str(record),
                "ttl": raw_data["ttl"],
            })

        return {
            "type": "records",
            "records": normalized,
        }