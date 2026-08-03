from core.models.finding import Finding


class ExpiryAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        valid_from = normalized_data.get(
            "valid_from",
        )

        valid_until = normalized_data.get(
            "valid_until",
        )

        if valid_from:

            findings.append(

                Finding(

                    category="TLS",

                    entity="Certificate",

                    name="valid_from",

                    value=valid_from,

                )

            )

        if valid_until:

            findings.append(

                Finding(

                    category="TLS",

                    entity="Certificate",

                    name="valid_until",

                    value=valid_until,

                )

            )

        return findings