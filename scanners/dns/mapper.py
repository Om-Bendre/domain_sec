from core.models.finding import Finding


class DNSMapper:

    def map(
        self,
        normalized_data,
        record_type,
    ):

        if normalized_data["type"] == "dnssec":

            return [
                Finding(
                    name="DNSSEC",
                    category="dns",
                    value="Enabled" if normalized_data["enabled"] else "Not Enabled",
                    metadata={
                        "dnskeys": (
                            [str(key) for key in normalized_data["dnskeys"]]
                            if normalized_data["dnskeys"] is not None
                            else []
                        )
                    },
                )
            ]

        findings = []

        for item in normalized_data["records"]:

            metadata = {}

            if item["ttl"] is not None:
                metadata["ttl"] = item["ttl"]

            findings.append(
                Finding(
                    name=f"{record_type} Record",
                    category="dns",
                    value=item["record"],
                    metadata=metadata,
                )
            )

        return findings