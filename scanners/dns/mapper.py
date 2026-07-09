from core.models.finding import Finding


class DNSMapper:
    """
    Converts normalized DNS data
    into SecureCheck Finding objects.
    """

    def map(
        self,
        normalized_data,
        record_type: str,
    ):

        findings = []

        for item in normalized_data:

            findings.append(

                Finding(

                    name=f"{record_type} Record",

                    category="dns",

                    value=item["record"],

                    metadata={
                        "ttl": item["ttl"]
                    }

                )

            )

        return findings