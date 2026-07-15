from core.models.finding import Finding


class TLSMapper:

    def map(
        self,
        normalized,
    ):

        findings = []

        for key, value in normalized.items():

            if value is None:
                continue

            findings.append(

                Finding(
                    name=key.replace("_", " ").title(),
                    category="tls",
                    value=str(value),
                    metadata={},
                )

            )

        return findings