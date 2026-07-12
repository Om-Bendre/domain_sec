from core.models.finding import Finding


class WHOISMapper:

    def map(
        self,
        normalized,
    ):

        findings = []

        for key, value in normalized.items():

            if isinstance(value, list):
                value = ", ".join(str(v) for v in value)

            findings.append(
                Finding(
                    name=key.replace("_", " ").title(),
                    category="whois",
                    value=str(value),
                    metadata={},
                )
            )

        return findings